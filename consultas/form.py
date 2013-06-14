from django.forms import forms, ModelForm

from consultas.models import Consulta

class ContactoForm(ModelForm):
    class Meta:
        model = Consulta
        exclude={'leido'}