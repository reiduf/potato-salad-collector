from django.contrib import admin
from .models import Potato, Comment, Store

# Register your models here.
admin.site.register(Potato)
admin.site.register(Comment)
admin.site.register(Store)