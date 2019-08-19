from django.contrib import admin

# Register your models here.
from .models import Post, Ticket

admin.site.register(Post)
admin.site.register(Ticket)
