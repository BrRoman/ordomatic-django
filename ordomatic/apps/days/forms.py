""" apps/tickets/forms.py """

from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict

from tempus_dominus.widgets import DatePicker, TimePicker

from .models import Day, DaySancto, DayTempo


class DayForm(forms.ModelForm):
    """ Form for Day (abstract). """
    name = forms.CharField()
    header = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': '3',
            }
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': '7',
            }
        ),
    )
    force = forms.ChoiceField(
        choices=[
            ('0', '0'),
            ('10', '10'),
            ('20', '20'),
            ('30', '30'),
            ('40', '40'),
            ('50', '50'),
            ('60', '60'),
            ('70', '70'),
            ('80', '80'),
            ('90', '90'),
            ('100', '100'),
            ('110', '110'),
            ('120', '120'),
        ],
    )

    class Meta:
        model = Day
        fields = [
            'calendar',
            'name',
            'header',
            'body',
            'force',
        ]


class DayTempoForm(DayForm):
    """ Form for DayTempo. """
    baseline = forms.ChoiceField(
        choices=[
            ('Start', 'Start'),
            ('Easter', 'Easter'),
            ('End', 'End'),
        ],
    )
    add = forms.IntegerField(
        max_value=365,
        min_value=-365,
    )

    class Meta:
        model = DayTempo
        fields = [
            'calendar',
            'name',
            'header',
            'body',
            'force',
            'baseline',
            'add',
        ]


class DaySanctoForm(DayForm):
    """ Form for DayTempo. """
    month = forms.ChoiceField(
        choices=[
            (1, 'January'),
            (2, 'February'),
            (3, 'March'),
            (4, 'April'),
            (5, 'May'),
            (6, 'June'),
            (7, 'July'),
            (8, 'August'),
            (9, 'September'),
            (10, 'October'),
            (11, 'November'),
            (12, 'December'),
        ],
    )
    day = forms.ChoiceField(
        choices=[(i + 1, i + 1) for i in range(31)],
    )

    class Meta:
        model = DaySancto
        fields = [
            'calendar',
            'name',
            'header',
            'body',
            'force',
            'month',
            'day',
        ]
