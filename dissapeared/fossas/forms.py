from django.forms import ModelForm
from .models import Fossas

class Fossas_Form(ModelForm):
    class Meta:
        model = Fossas
        exclude = ['address', 'lat', 'lng']

class Fossas_Update(ModelForm):
    class Meta:
        model = Fossas
        exclude = ['address', 'lat', 'lng']
