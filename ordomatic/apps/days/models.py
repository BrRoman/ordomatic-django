""" apps/days/models.py """

from django.db import models


class Day(models.Model):
    """ Abstract day model. """
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

    def __str__(self):
        return self.name


class DayTempo(Day):
    """ Day tempo model. """
    baseline = models.CharField(
        max_length=25,
    )
    add = models.IntegerField()


class DaySancto(Day):
    """ Day sancto model. """
    month = models.IntegerField()
    day = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(
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
            self.day
        )
