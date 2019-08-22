from django.contrib import admin

# Register your models here.
from .models import CUser, PUser

admin.site.register(CUser)
admin.site.register(PUser)