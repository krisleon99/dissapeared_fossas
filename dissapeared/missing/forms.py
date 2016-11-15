from django.forms import ModelForm
from .models import Physical_Description
from .models import Origin
from .models import Place_Missing
from .models import Missing

class Missing_Form(ModelForm):
    class Meta:
        model = Missing

class Missing_Update(ModelForm):
    class Meta:
        model = Missing

class Origin_Form(ModelForm):
    class Meta:
        model = Origin

class Origin_Update(ModelForm):
    class Meta:
        model = Origin

class Place_Form(ModelForm):
    class Meta:
        model = Place_Missing
        exclude = ['lat', 'lng']

class Place_Update(ModelForm):
    class Meta:
        model = Place_Missing
        exclude = ['lat', 'lng']

class Physical_Description_Form(ModelForm):
    class Meta:
        model = Physical_Description

class Physical_Description_Update(ModelForm):
    class Meta:
        model = Physical_Description
