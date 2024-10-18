from datetime import datetime, timedelta


def get_days_from_today(date):

    today = datetime.today().date()

    try:
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
        difference = (today - given_date).days
        return difference
    except ValueError:
        return f'Use a different format'


print(get_days_from_today("2020-10-2"))
