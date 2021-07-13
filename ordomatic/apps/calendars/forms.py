""" apps/calendars/forms.py """

from django import forms

from .models import Calendar


class CalendarForm(forms.ModelForm):
    """ Form for Calendar. """
    name = forms.CharField()
    base = forms.ChoiceField(
        choices=[
            ('OF', 'Ordinary Form'),
            ('EF', 'Extraordinary Form'),
        ],
    )

    class Meta:
        model = Calendar
        fields = '__all__'
