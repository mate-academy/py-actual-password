import datetime
import pytest

from app.main import actual_password


@pytest.mark.parametrize(
    "days, expected",
    [
        (0, "Password is actual."),
        (1, "Password is actual."),
        (15, "Password is actual."),
        (29, "Password is actual."),
        (30, "Password is actual."),

    ],
)
def test_30_days_or_less(days, expected):
    today = datetime.date.today()
    actual_date = today - datetime.timedelta(days)
    year = actual_date.year
    month = actual_date.month
    day = actual_date.day
    assert actual_password(year, month, day) == expected


@pytest.mark.parametrize(
    "days, expected",
    [
        (31, "You should change your password."),
        (45, "You should change your password."),
        (50, "You should change your password."),
        (59, "You should change your password."),
        (60, "You should change your password."),

    ],
)
def test_more_30_days_less_60(days, expected):
    today = datetime.date.today()
    actual_date = today - datetime.timedelta(days)
    year = actual_date.year
    month = actual_date.month
    day = actual_date.day
    assert actual_password(year, month, day) == expected


@pytest.mark.parametrize(
    "days, expected",
    [
        (61, "Immediately change the password!"),
        (99, "Immediately change the password!"),
        (100, "Immediately change the password!"),
        (1000, "Immediately change the password!"),
        (10000, "Immediately change the password!"),

    ],
)
def test_more_60_days(days, expected):
    today = datetime.date.today()
    actual_date = today - datetime.timedelta(days)
    year = actual_date.year
    month = actual_date.month
    day = actual_date.day
    assert actual_password(year, month, day) == expected
