from django.db import models
from django.db.models.deletion import CASCADE
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidades', max_length=50)
    # Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades empleados'

    def __str__(self):
        return f'{self.id} - {self.habilidad}'
    

class Empleado (models.Model):
    # Modelo para tabla empleado

    # Contador
    # Administrador
    # Economista
    # Otro
    job_choices = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Gestor de Recursos Humanos'),
        ('4', 'Analista de Gerencia'),
        ('5', 'Otro'),
    )
    
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField(
        'Nombres completos',
        max_length=120,
        blank=True
    )
    job = models.CharField('Trabajo',max_length=1, choices=job_choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', null= True, blank=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Listado de personas'
        ordering = ['first_name']
        unique_together = (
            'first_name',
            'last_name',
        )
      
    def __str__(self) -> str:
        return f'{self.id} - {self.first_name} - {self.last_name}'


