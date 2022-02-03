import datetime


def actual_password(year, month, day):
    today = datetime.date.today()
    password_time = datetime.date(year, month, day)
    if (today - password_time).days > 60:
        return "Immediately change the password!"
    if (today - password_time).days > 30:
        return "You should change your password."
    return "Password is actual."
