from datetime import datetime

from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect, HttpResponse, request
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import Http404
from django.template import RequestContext

from web.models import Noticias,BlogEntry, Libros, Visita, auction, bid
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import user_logged_in
from django.utils.encoding import force_text
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import LOGINFORM, VisitaForm
"""
from django_registration import signals
from django_registration.exceptions import ActivationError
from django_registration.forms import RegistrationForm
"""
# Create your views here.
from django.views.generic import TemplateView, FormView, DetailView, CreateView


class index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,  **kwargs):
        context=super(index, self).get_context_data(**kwargs)
        context['visitas']= Visita.objects.all()[0:5:-1]
        context['not']= Noticias.objects.all()[0:5:-1]
        context['poesia']=Libros.objects.filter(tipolib='Poesia')
        context['rel']= Libros.objects.filter(tipolib='Relato corto')
        #context['preorders']= 100 - Preorder.objects.all().count()
        return context


class blog(TemplateView):
    template_name = 'blog.html'
    def get_context_data(self,  **kwargs):
        context=super(blog, self).get_context_data(**kwargs)
        context['blogentry']= BlogEntry.objects.all()[0:5:-1]
        context['visitas']= Visita.objects.all()[0:5:-1]
        return context


class libros(TemplateView):
    template_name = 'libros.html'
    def get_context_data(self,  **kwargs):
        context=super(libros, self).get_context_data(**kwargs)
        context['poesia']=Libros.objects.filter(tipolib='Poesia')
        context['rel']= Libros.objects.filter(tipolib='Relato corto')
        context['visitas']= Visita.objects.all()[0:5:-1]

        return context


class subasta(LoginView):
    template_name = 'subastas.html'
    form_class = LOGINFORM
    success_url = reverse_lazy('web:Subastas')
    def get_context_data(self,  **kwargs):
        context=super(subasta, self).get_context_data(**kwargs)
        context['form']=LOGINFORM
        context['user']=User
        context['Subastas']= auction.objects.all()[:3]
        return context


class visita(CreateView):
    form_class = VisitaForm
    template_name = 'visitas.html'
    success_url = '../'
    model = Visita

    def get_context_data(self, **kwargs):
        context=super(visita, self).get_context_data()
        context['form']=VisitaForm
        context['visitas']= Visita.objects.all()[0:5:-1]

        return context

    def get_form_kwargs(self):
        kwargs = super(visita, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class librodetail(TemplateView):
    template_name = 'libros_detail.html'

    def get_context_data(self, **kwargs):
        context= super(librodetail, self).get_context_data()
        context['lista_libros']=Libros.objects.filter(id=kwargs['pk'])
        context['visitas']= Visita.objects.all()[0:5:-1]

        return context


class descarga(TemplateView):
    template_name = 'descarga.html'

    def get_context_data(self,  **kwargs):
        context=super(descarga, self).get_context_data(**kwargs)
        context['libro']= Libros.objects.filter(id=kwargs['pk'])
        context['visitas']= Visita.objects.all()[0:5:-1]

        context['video']=Video.objects.filter(id=1)
        return context

class donacion(TemplateView):
    template_name = 'donacion.html'

    def get_context_data(self,  **kwargs):
        context=super(donacion, self).get_context_data(**kwargs)
        context['libro']= Libros.objects.filter(id=kwargs['pk'])
        context['visitas']= Visita.objects.all()[0:5:-1]


        return context


class leer(TemplateView):
    template_name = 'leer.html'
    def get_context_data(self,  **kwargs):
        context=super(leer, self).get_context_data(**kwargs)
        context['visitas']= Visita.objects.all()[0:5:-1]

        context['libro']= Libros.objects.filter(id=kwargs['pk'])
        return context
"""
class preventa(CreateView):
    form_class = PreorderForm
    template_name = 'preorder.html'
    success_url = '../success'
    model = Preorder

    def get_context_data(self, **kwargs):
        context = super(preventa, self).get_context_data()
        context['form'] = PreorderForm
        return context

    def get_form_kwargs(self):
        kwargs = super(preventa,self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

"""

class success(TemplateView):
    template_name = 'success_preorder.html'


class aviso(TemplateView):
    template_name = 'aviso.html'


class privacidad(TemplateView):
    template_name = 'privacidad.html'


class cookies(TemplateView):
    template_name = 'cookies.html'


class terminos(TemplateView):
    template_name = 'terminos.html'

"""
from django.contrib.auth import authenticate, get_user_model, login
from django.urls import reverse_lazy

from django_registration import signals
from django_registration.views import RegistrationView as BaseRegistrationView


User = get_user_model()


class RegistrationView(BaseRegistrationView):


    success_url = reverse_lazy("django_registration_complete")

    def register(self, form):
        new_user = form.save()
        new_user = authenticate(
            **{
                User.USERNAME_FIELD: new_user.get_username(),
                "password": form.cleaned_data["password1"],
            }
        )
        login(self.request, new_user)
        signals.user_registered.send(
            sender=self.__class__, user=new_user, request=self.request
        )
        return new_user



USER_MODEL_MISMATCH =


class RegistrationView(FormView):
  

    disallowed_url = reverse_lazy("django_registration_disallowed")
    form_class = RegistrationForm
    success_url = 'Subastas'
    template_name = "registration/registration_form.html"

    def dispatch(self, *args, **kwargs):
       
        if not self.registration_allowed():
            return HttpResponseRedirect(force_text(self.disallowed_url))
        return super().dispatch(*args, **kwargs)

    def get_form(self, form_class=None):
       
        if form_class is None:
            form_class = self.get_form_class()
        form_model = form_class._meta.model
        user_model = get_user_model()
        if form_model._meta.label != user_model._meta.label:
            raise ImproperlyConfigured(
                USER_MODEL_MISMATCH.format(
                    view=self.__class__,
                    form=form_class,
                    form_model=form_model,
                    user_model=user_model,
                )
            )
        return form_class(**self.get_form_kwargs())

    def get_success_url(self, user=None):
       
        # This is overridden solely to allow django-registration to
        # support passing the user account as an argument; otherwise,
        # the base FormMixin implementation, which accepts no
        # arguments, could be called and end up raising a TypeError.
        return super().get_success_url()

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url(self.register(form)))

    def registration_allowed(self):
        
        return getattr(settings, "REGISTRATION_OPEN", True)

    def register(self, form):
        
        raise NotImplementedError


class ActivationView(TemplateView):
    

    success_url = None
    template_name = "django_registration/activation_failed.html"

    def get_success_url(self, user=None):
        
        return force_text(self.success_url)

    def get(self, *args, **kwargs):
       
        extra_context = {}
        try:
            activated_user = self.activate(*args, **kwargs)
        except ActivationError as e:
            extra_context["activation_error"] = {
                "message": e.message,
                "code": e.code,
                "params": e.params,
            }
        else:
            signals.user_activated.send(
                sender=self.__class__, user=activated_user, request=self.request
            )
            return HttpResponseRedirect(
                force_text(self.get_success_url(activated_user))
            )
        context_data = self.get_context_data()
        context_data.update(extra_context)
        return self.render(context_data)

    def activate(self, *args, **kwargs):
       
        raise NotImplementedError

def bid_auction(request, id):
    if request.user.is_authenticated():
        if request.method == 'POST':

            amount = request.POST['am']
            auct = auction.objects.filter(id=id)
            if auct:
                auct = auction.objects.get(id=id)
            else:
                msg = "Auction not found"
                return render("auction.html", {'msg': msg}, context_instance= RequestContext(request))

            if auct.lock == True:
                return render("lock.html", context_instance = RequestContext(request))

            if auct.lifecycle != 'A':
                msg = "Auction not active"
                return render("auction.html", {'auct':auct, 'msg': msg}, context_instance= RequestContext(request))
            if request.user == auct.seller:
                msg = "Can not bid on your own auction"
                return render("auction.html", {'auct':auct, 'msg': msg}, context_instance= RequestContext(request))
            if auct.min_price > float(amount) or (float(amount) - auct.min_price < 0.01):
                msg = "Amount have to be at least 0.01 bigger than minimum price."
                return render("auction.html", {'auct':auct, 'msg': msg}, context_instance= RequestContext(request))

            prev_bid_wining = bid.objects.filter(status='W', auct=auct)
            if prev_bid_wining:
                prev_bid_wining = bid.objects.filter(status='W', auct=auct).get()

            #in case that exists
            if prev_bid_wining:
                if prev_bid_wining.user == request.user:
                    msg = "You are already wining this auction."
                    return render("auction.html", {'auct':auct,'bb':prev_bid_wining, 'msg': msg}, context_instance= RequestContext(request))

                if float(amount) - prev_bid_wining.amount < 0.01:
                    msg = "Bid has to be at less 0.01 bigger than previous bids."
                    return render("auction.html", {'auct':auct,'bb':prev_bid_wining, 'msg': msg}, context_instance= RequestContext(request))

                send_mail('Bid losing.', "Somebody bid in the same auction that you did.", 'no_repli@yaas.com', [prev_bid_wining.user.email,], fail_silently=False)
                prev_bid_wining.status = 'L'
                prev_bid_wining.save()

            b = bid(user=request.user, amount=float(amount), auct=auct, status='W')
            b.save()

            #Optional feature: soft deadlines
            deadline = auct.deadline.strftime("%d/%m/%Y %H:%M:%S")
            d = datetime.datetime.strptime(deadline, "%d/%m/%Y %H:%M:%S")

            if (d - datetime.datetime.now()).total_seconds() < 350:
                auct.deadline = auct.deadline + datetime.timedelta(seconds = 350)
                auct.save()

            send_mail('New bid in your auction.', "Somebody bid in the one of your auctions.", 'no_repli@yaas.com', [auct.seller.email,], fail_silently=False)
            send_mail('Bid accepted.', "Your new bed has been acepted.", 'no_repli@yaas.com', [request.user.email,], fail_silently=False)

            msg = "Bid saved sucesfully."
            return render("auction.html", {'auct':auct,'bb':b, 'msg': msg}, context_instance= RequestContext(request))

        else:
            auct = auction.objects.filter(id=id)
            if auct:
                auct = auction.objects.get(id=id)
            else:
                msg = "Auction not found"
                return render("auction.html", {'msg': msg}, context_instance= RequestContext(request))

            b = bid.objects.filter(status='W', auct=auct)
            if b:
                b = bid.objects.filter(status='W', auct=auct).get()
            return render("auction.html", {'auct':auct, 'bb':b}, context_instance= RequestContext(request))

    else:
        mesg = _("You have to log in first")
        posts = auction.objects.all()
        return render("home.html", {'msg': mesg, 'posts': posts}, context_instance= RequestContext(request))


def view_auction(request, id):
    auct = auction.objects.filter(id = id)
    if auct:
        auct = auction.objects.get(id = id)

        if auct.lock == True:
            return render("lock.html", context_instance = RequestContext(request))

        bb = bid.objects.filter(status='W', auct=auct)
        if bb:
            bb = bid.objects.filter(status='W', auct=auct).get()
        return render("auction.html", {'auct': auct, 'bb': bb}, context_instance= RequestContext(request))
    else:
        mesg = _("Auction not found.")
        posts = auction.objects.all()
        return render("home.html", {'msg': mesg, 'posts': posts}, context_instance= RequestContext(request))

"""
class Profile(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context['User'] = user_logged_in

        return context

class Logout(LogoutView):
    template_name = 'registration/logout.html'