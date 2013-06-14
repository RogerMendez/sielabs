from django.db import models

class Consulta(models.Model):
    nombre = models.CharField(max_length='50', verbose_name="")
    email = models.EmailField(verbose_name="")
    descripcion = models.TextField(verbose_name="")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="")
    leido = models.IntegerField(default=0, verbose_name="")
    def __unicode__(self):
        return self.nombre