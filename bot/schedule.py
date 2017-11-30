from bot.garbage import TYPE


class Scedule:
    def __init__(self):
        WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                    'Friday', 'Saturday', 'Sunday']

        self.SCHEDULE = [None,
                         [TYPE['used_paper'], TYPE['pet']],
                         [TYPE['burnable']],
                         None,
                         [TYPE['bottle'], TYPE['can'], TYPE['plastic']],
                         [TYPE['burnable']],
                         None]

    def of_date(self, date):
        from math import ceil
        week_of_month = ceil(date.day / 7)
        weekday = date.weekday()

        if (week_of_month == 1 or week_of_month == 3) and (weekday == 1):
            sp_schedule = self.SCHEDULE[weekday].copy()
            sp_schedule.append(TYPE['unburnable'])
            return sp_schedule
        else:
            return self.SCHEDULE[weekday]

    def of_weekday(self, weekday):
        return self.SCHEDULE[weekday]
