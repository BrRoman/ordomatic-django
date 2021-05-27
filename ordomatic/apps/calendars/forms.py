""" apps/calendars/forms.py """

from django import forms

from .models import Calendar


class CalendarForm(forms.ModelForm):
    """ Form for Calendar. """
    name = forms.CharField()

    class Meta:
        model = Calendar
        fields = '__all__'
