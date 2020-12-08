"""MASKWEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.contrib.auth.views import LogoutView
from MASKWEB import settings
from web.views import index, Profile, Logout,blog, libros, subasta, visita, librodetail, donacion, descarga,aviso,privacidad,cookies,terminos, leer

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index.as_view(), name='Index'),
    url(r'^blog/', blog.as_view(),name='Blog'),
    url(r'^libros/', libros.as_view(),name='Libros'),
    url(r'^subastas/', subasta.as_view(),name='Subastas'),
    url(r'visita/',visita.as_view(),name='Visita'),
    url(r'librodetail/(?P<pk>\d+)',librodetail.as_view(),name='LibroDetail'),
    url(r'^leer/(?P<pk>\d+)',leer.as_view(),name='Leer'),
    #url(r'^preorder/',preventa.as_view(), name = "Preorder"),
    url(r'^donaciones/(?P<pk>\d+)',donacion.as_view(), name='Donacion'),
    #url(r'^success/',success.as_view(),name='Success'),
    url(r'^descarga/(?P<pk>\d+)',descarga.as_view(),name='Descarga'),
    url(r'^logout/', LogoutView.as_view() , {'next_page': settings.LOGOUT_REDIRECT_URL},name='LogOut'),
    #url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    #url(r'^accounts/', include('django_registration.auth_urls')),
    url(r'^accounts/profile',Profile.as_view(),name='Profile'),
    url(r'^aviso/', aviso.as_view(), name='aviso'),
    url(r'^privacidad/', privacidad.as_view(), name='privacidad'),
    url(r'^cookies/', cookies.as_view(), name='cookies'),
    url(r'^terminos/', terminos.as_view(), name='terminos'),
    #url(r'^auction/(?P<id>\w+)/$', view_auction),
    #url(r'^bidauction/(?P<id>\w+)/$', bid_auction),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
