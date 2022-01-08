from .models import Imag 
from django import forms
class Images(forms.ModelForm):
  class Meta:
    model = Imag 
    fields =('Image', )
