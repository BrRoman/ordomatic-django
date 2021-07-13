""" utils/utils.py """

from apps.days.models import DaySancto, DayTempo

ORDINALS = [
    'First',
    'Second',
    'Thirst',
    'Fourth',
    'Fifth',
    'Sixth',
    'Seventh',
]
WEEKDAYS = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
]


def populate(calendar):
    """ Populate the given calendar with the default days of EF. """
    return(calendar)
