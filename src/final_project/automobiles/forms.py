from django.forms import ModelForm
from .models import Automobile


class AutomobileForm(ModelForm):
    class Meta:
        model = Automobile
        fields = '__all__'


