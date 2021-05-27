""" apps/ordos/forms.py """

from django import forms

from .models import Ordo


class OrdoForm(forms.ModelForm):
    """ Form for Ordo. """
    name = forms.CharField()

    class Meta:
        model = Ordo
        fields = '__all__'
