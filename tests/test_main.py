import datetime
import random

import pytest

from app.main import actual_password


def thirty_days_or_less():
    today = datetime.date.today()
    random_day = random.randint(1, 30)

    result_date = today - datetime.timedelta(days=random_day)
    return result_date


thirty_days = thirty_days_or_less()


@pytest.mark.parametrize(
    "year, month, day, expected",
    [
        (
                thirty_days.year,
                thirty_days.month,
                thirty_days.day,
                "Password is actual."
        ),
    ],
)
def test_30_days_or_less(year, month, day, expected):
    assert actual_password(year, month, day) == expected


def more_thirty_days_less_sixty():
    today = datetime.date.today()
    random_day = random.randint(31, 60)

    result_date = today - datetime.timedelta(days=random_day)
    return result_date


more_thirty_less_sixty = more_thirty_days_less_sixty()


@pytest.mark.parametrize(
    "year, month, day, expected",
    [
        (
                more_thirty_less_sixty.year,
                more_thirty_less_sixty.month,
                more_thirty_less_sixty.day,
                "You should change your password."
        ),
    ],
)
def test_more_30_days_less_60(year, month, day, expected):
    assert actual_password(year, month, day) == expected


def more_sixty_days():
    today = datetime.date.today()
    random_day = random.randint(61, 10000)

    result_date = today - datetime.timedelta(days=random_day)
    return result_date


sixty_days = more_sixty_days()


@pytest.mark.parametrize(
    "year, month, day, expected",
    [
        (
                sixty_days.year,
                sixty_days.month,
                sixty_days.day,
                "Immediately change the password!"
        ),
    ],
)
def test_more_60_days(year, month, day, expected):
    assert actual_password(year, month, day) == expected
