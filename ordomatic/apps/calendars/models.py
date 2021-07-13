""" apps/calendars/models.py """

from django.contrib.auth.models import User
from django.db import models


class Calendar(models.Model):
    """ Calendar model. """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
    )
    name = models.CharField(
        max_length=255,
    )
    base = models.CharField(
        max_length=2,
        choices=[
            ('OF', 'Ordinary Form'),
            ('EF', 'Extraordinary Form'),
        ]
    )

    def __str__(self):
        return self.name
