from django.forms import ModelForm
from .models import AuthorModel

class AuthorForm(ModelForm):
    class Meta:
        model = AuthorModel
        fields = '__all__'
