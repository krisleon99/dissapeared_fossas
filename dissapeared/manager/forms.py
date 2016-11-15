from django.forms import ModelForm
from django.contrib.auth.models import User

class User_Basic_Update(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class User_Change_Password(ModelForm):
    class Meta:
        model = User
        fields = ['password']
