from django.forms import ModelForm
from .models import *

class ADD_form(ModelForm):

    class Meta:

        model = Product
        fields='__all__'

