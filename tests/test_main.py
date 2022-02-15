import datetime

import pytest

from app.main import actual_password


@pytest.mark.parametrize(
    "days", [0, 15, 30],
)
def test_should_check_if_have_passed_30_days_or_less(days):
    today = datetime.date.today()
    check_date = today - datetime.timedelta(days)
    year = check_date.year
    month = check_date.month
    day = check_date.day
    assert actual_password(year, month, day) == "Password is actual."


@pytest.mark.parametrize(
    "days", [31, 45, 60],
)
def test_should_check_if_have_passed_from_31_to_60_days(days):
    today = datetime.date.today()
    check_date = today - datetime.timedelta(days)
    year = check_date.year
    month = check_date.month
    day = check_date.day
    assert actual_password(year, month, day) ==\
        "You should change your password."


@pytest.mark.parametrize(
    "days", [61, 145, 1000],
)
def test_should_check_if_have_passed_more_than_60_days(days):
    today = datetime.date.today()
    check_date = today - datetime.timedelta(days)
    year = check_date.year
    month = check_date.month
    day = check_date.day
    assert actual_password(year, month, day) ==\
        "Immediately change the password!"
