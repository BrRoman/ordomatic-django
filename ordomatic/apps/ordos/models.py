""" apps/ordos/models.py """

from django.contrib.auth.models import User
from django.db import models


class Ordo(models.Model):
    """ Ordo model. """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
    )
    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.name
