from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import request, response
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
"""from django_registration import validators
from django_registration.users import UserModel
from django_registration.users import UsernameField
"""
from web.models import Visita


class VisitaForm(forms.ModelForm):


    class Meta:
        model=Visita
        fields=['nombre','comentario',]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
"""
class PreorderForm(forms.ModelForm):
    class Meta:
        model= Preorder
        fields=['tu_nombre','enviar_a','email','dedicatoria','deseo']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def send_mail(self, request):
        if request.HttpRequest.method == 'POST':
            form = PreorderForm(request.HttpRequest.POST)
            if form.is_valid():
                form.save()
                return send_mail('MASKDUMORTE--BookPreorder',
                                 'Usted ha hecho un pedido a maskdumorte.com, nos encargaremos de hacerselo llegar a: ' + self.enviar_a + ' si tiene alguna duda o problema refierase a iago.otero.84@gmail.com',
                                 'iago.otero.84@gmail.com', ['iago.otero.84@gmail.com', self.email])



"""

"""


class RegistrationForm(UserCreationForm):




    class Meta(UserCreationForm.Meta):
        fields = [
            User.USERNAME_FIELD,
            User.get_email_field_name(),
            "password1",
            "password2",
        ]

    error_css_class = "error"
    required_css_class = "required"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        email_field = User.get_email_field_name()
        if hasattr(self, "reserved_names"):
            reserved_names = self.reserved_names
        else:
            reserved_names = validators.DEFAULT_RESERVED_NAMES
        username_validators = [
            validators.ReservedNameValidator(reserved_names),
            validators.validate_confusables,
        ]
        self.fields[User.USERNAME_FIELD].validators.extend(username_validators)
        self.fields[email_field].validators.extend(
            (validators.HTML5EmailValidator(), validators.validate_confusables_email)
        )
        self.fields[email_field].required = True


class RegistrationFormCaseInsensitive(RegistrationForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[User.USERNAME_FIELD].validators.append(
            validators.CaseInsensitiveUnique(
                User, User.USERNAME_FIELD, validators.DUPLICATE_USERNAME
            )
        )


class RegistrationFormTermsOfService(RegistrationForm):
 

    tos = forms.BooleanField(
        widget=forms.CheckboxInput,
        label=("I have read and agree to the Terms of Service"),
        error_messages={"required": validators.TOS_REQUIRED},
    )


class RegistrationFormUniqueEmail(RegistrationForm):
  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        email_field = User.get_email_field_name()
        self.fields[email_field].validators.append(
            validators.CaseInsensitiveUnique(
                User, email_field, validators.DUPLICATE_EMAIL
            )
        )



class ResendActivationForm(forms.Form):
    required_css_class = 'required'
    email = forms.EmailField(label=("E-mail"))

"""
class LOGINFORM(AuthenticationForm):

    model= User


