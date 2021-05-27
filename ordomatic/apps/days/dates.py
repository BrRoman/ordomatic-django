""" apps/main/dates.py """

from datetime import date
from math import floor


def calculate_easter(year):
    """ Return Easter date of given year. """
    # Source(in French): https: // fr.wikipedia.org/wiki/Calcul_de_la_date_de_Pâques
    # See also: https: // en.wikipedia.org/wiki/Computus.
    metonic_cycle = year % 19
    hundred = floor(year / 100)
    rank = year % 100
    bissextile_century_quotient = floor(hundred / 4)
    bissextile_century_remainder = hundred % 4
    proemptose_cycle = floor((hundred + 8) / 25)
    proemptose = floor(
        (
            hundred
            - proemptose_cycle
            + 1
        ) / 3
    )
    epact = (
        19 * metonic_cycle
        + hundred
        - bissextile_century_quotient
        - proemptose
        + 15
    ) % 30
    bissextile_year_quotient = floor(rank / 4)
    bissextile_year_remainder = rank % 4
    dominical_letter = (
        2 * bissextile_century_remainder
        + 2 * bissextile_year_quotient
        - epact
        - bissextile_year_remainder
        + 32
    ) % 7
    correction = floor(
        (metonic_cycle + 11 * epact + 22 * dominical_letter) / 451)
    month = floor(
        (
            epact
            + dominical_letter
            - 7 * correction
            + 114
        )
        / 31
    )
    day = (
        epact
        + dominical_letter
        - 7 * correction
        + 114
    ) % 31
    return date(year, month, day + 1)
