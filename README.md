# Actual password

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

Write tests for the `actual_password` function. This function:

- takes three numbers: `year` - year, `month` - month, `day` - the day 
when the password was last updated;
- converts the received numbers into a date and checks how many days have passed since that date;
- returns a message about whether to change the password.

If 30 days or less have passed since the last password change, 
the function returns the message `Password is actual.`.

If more than 30 days have passed since the last password change, 
the function returns the message `You should change your password.`. 

If more than 60 days have passed since the last password change, 
the function returns the message `Immediately change the password!`.

Examples (let it be Jun 10, 2021 for today):
```python
actual_password(2020, 6, 9) == "Immediately change the password!"
actual_password(2021, 6, 1) == "Password is actual."
actual_password(2021, 5, 1) == "You should change your password."
```