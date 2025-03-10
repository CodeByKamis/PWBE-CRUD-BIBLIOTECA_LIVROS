from django import forms
from .models import Livros

class ItemForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = '__all__'
        # '__all__' usa quando você quer tudo
        # ['nome', 'descricao'] usa quando você ter alguns campos específicos ou apenas um campo 