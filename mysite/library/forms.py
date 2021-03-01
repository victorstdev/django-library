from django import forms
from .models import Livro, Reserva

class DateInput(forms.DateInput):
    input_type = 'date'


class CadastrarLivroForm(forms.ModelForm):
    
    class Meta:
        model = Livro
        fields = '__all__'

class UpdateLivroForm(forms.ModelForm):
    
    class Meta:
        model = Livro
        fields = '__all__'
