from django.db import models
from volunteers.models import VoluntaryUser
# Create your models here.


class Task (models.Model):
    voluntary = models.ForeignKey(VoluntaryUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks', verbose_name='Voluntário Responsável')
    title = models.CharField(max_length=255, verbose_name='Título')
    # Campo para espaço como chave estrangeira de espaços cadastrados
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    expected_date = models.DateField(blank=True, null=True, verbose_name='Data prevista')
    prevision_hours = models.TimeField(blank=True, null=True, verbose_name='Horário previsto')
    volunteers = models.ManyToManyField(VoluntaryUser, blank=True, related_name='volunteers', verbose_name='Voluntários envolvidos')
    status_completed = models.BooleanField(default=False, verbose_name='Status da tarefa')
    details = models.TextField(null=True, blank=True, verbose_name='Detalhes')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
