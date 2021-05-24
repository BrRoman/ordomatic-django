""" apps/ordos/models.py """

from django.db import models


class Ordo(models.Model):
    """ Ordo model. """
    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.name
