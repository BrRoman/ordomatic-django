""" apps/days/models.py """

from django.db import models

from apps.calendars.models import Calendar


class Day(models.Model):
    """ Abstract day model. """
    calendar = models.ForeignKey(
        Calendar,
        on_delete=models.CASCADE,
        blank=True,
    )
    name = models.CharField(
        null=True,
        max_length=255,
    )
    header = models.TextField(
        null=True,
    )
    body = models.TextField(
        null=True,
    )
    force = models.PositiveIntegerField(
        null=True,
    )

    class Meta:
        abstract = True


class DayTempo(Day):
    """ Day tempo model. """
    baseline = models.CharField(
        max_length=25,
    )
    add = models.IntegerField()

    def __str__(self):
        return '{} (of calendar {})'.format(self.name, self.calendar)


class DaySancto(Day):
    """ Day sancto model. """
    month = models.IntegerField()
    day = models.IntegerField()

    def __str__(self):
        return '{} {} (of calendar {})'.format(
            [
                'January',
                'February',
                'March',
                'April',
                'May',
                'June',
                'July',
                'August',
                'September',
                'October',
                'November',
                'December',
            ][self.day - 1],
            self.day,
            self.calendar
        )
