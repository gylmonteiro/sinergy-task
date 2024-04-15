from django.db import models
from volunteers.models import VoluntaryUser
# Create your models here.
class Task (models.Model):
    voluntary = models.ForeignKey(VoluntaryUser, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Voluntário')
    title = models.CharField(max_length=255, verbose_name='Título')
    # Campo para espaço como chave estrangeira de espaços cadastrados
    created_at = models.DateTimeField(verbose_name='Data de criação')
    created_up = 