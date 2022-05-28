from freezegun import freeze_time
from app.main import actual_password


@freeze_time("2021-06-10")
class TestActualPassword:
    def test_return_immediately_change_if_password_is_older_60_days(self):
        assert actual_password(2020, 6, 9) == "Immediately change the password!"

    def test_return_should_change_if_password_is_older_30_days(self):
        assert actual_password(2021, 5, 1) == "You should change your password."

    def test_return_is_actual_if_password_is_younger_30_days(self):
        assert actual_password(2021, 6, 1) == "Password is actual."
