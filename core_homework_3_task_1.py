from datetime import datetime
today = datetime.today()
def get_days_from_today(date):
    try:
        given_date = datetime.fromisoformat(date)
        return int(today.toordinal() - given_date.toordinal())
    except ValueError:
        return "The date is not correct"
print(get_days_from_today("07-10-2024"))
