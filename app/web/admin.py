from django.contrib import admin
from web.models import Libros, BlogEntry,Visita, Noticias
# Register your models here.

from .models import auction, bid

admin.site.register(auction)
admin.site.register(bid)
admin.site.register(Libros)
admin.site.register(BlogEntry)
admin.site.register(Noticias)
admin.site.register(Visita)

