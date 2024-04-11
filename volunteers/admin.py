from django.contrib import admin
from .models import VoluntaryUser
# Register your models here.

@admin.register(VoluntaryUser)
class VoluntaryUserAdmin(admin.ModelAdmin):
    list_display = ('username',)