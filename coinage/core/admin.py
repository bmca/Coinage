from django.contrib import admin
from core.models import Game, Usuario, Comentario
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django_facebook.models import FacebookCustomUser

# Register your models here.
admin.site.register(Game)
admin.site.register(Usuario)
admin.site.register(Comentario)
admin.site.register([FacebookCustomUser])
UserAdmin.list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')