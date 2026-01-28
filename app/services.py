from datetime import date
from dateutil.relativedelta import relativedelta

def calculate_age(dob: date):
    today = date.today()

    if dob > today:
        raise ValueError("Date of birth cannot be in the future")

    age = relativedelta(today, dob)

    return {
        "years": age.years,
        "months": age.months,
        "days": age.days
    }
