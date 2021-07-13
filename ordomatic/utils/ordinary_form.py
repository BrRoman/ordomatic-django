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
    """ Populate the given calendar with the default days of OF. """
    # TEMPORAL:
    # Advent:
    for week in range(4):
        for day in range(7):
            if day == 0:
                header = '{} Sunday of Advent'.format(ORDINALS[week])
            else:
                header = '{} after {} Sunday of Advent'.format(
                    WEEKDAYS[day], ORDINALS[week].lower())
            DayTempo.objects.create(
                calendar=calendar,
                name='adv_{}_{}'.format(week, day),
                baseline='start',
                add=week * 7 + day,
                force=110 if day == 0 else 20,
                header=header,
            )
    # From 17 December to Christmas:
    for day in range(17, 25):
        DaySancto.objects.create(
            calendar=calendar,
            name='last_days_before_christmas_{}'.format(day),
            month=12,
            day=day,
            force=90,
            header='Feria',
        )
    # Christmas:
    for day in range(7):
        if day == 0:
            header = 'Christmas - Solennity with octave'
        else:
            header = 'Octave of Christmas'
        DayTempo.objects.create(
            calendar=calendar,
            name='christmas_{}'.format(day),
            baseline='christmas',
            add=day,
            force=100,
            header=header,
        )

    # SANCTORAL:
    DaySancto.objects.create(
        calendar=calendar,
        name='11_30',
        month=11,
        day=30,
        force=70,
        header='Saint Andrew, Apostle - Feast',
    )
    DaySancto.objects.create(
        calendar=calendar,
        name='12_03',
        month=12,
        day=3,
        force=40,
        header='Saint Franciscus Xavier - Memory',
    )
    DaySancto.objects.create(
        calendar=calendar,
        name='12_07',
        month=12,
        day=7,
        force=40,
        header='Saint Ambrosius - Memory',
    )
    DaySancto.objects.create(
        calendar=calendar,
        name='12_08',
        month=12,
        day=8,
        force=100,
        header='The Immaculate Conception of the Blessed Virgin - Solennity',
    )


def populate_extraordinary_form(calendar):
    """ Populate the given calendar with generic days of EF. """
    return(calendar)
