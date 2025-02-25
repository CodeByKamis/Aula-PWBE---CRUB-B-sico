from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        # '__all__' usa cuqnaod vc quer tudo
        # ['nome', 'descricao'] usa quando você ter alguns campos específicos ou apenas um campo 