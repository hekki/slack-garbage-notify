from bot.garbage import TYPE


class Scedule:
    def __init__(self):
        WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                    'Friday', 'Saturday', 'Sunday']

        self.BASE_SCHEDULE = [[TYPE['burnable'], TYPE['unburnable'], TYPE['spray_can'], TYPE['dry_cell']],
                              [TYPE['plastic']],
                              None,
                              None,
                              [TYPE['burnable'], TYPE['unburnable'], TYPE['spray_can'], TYPE['dry_cell']],
                              [TYPE['used_paper'], TYPE['cloth'], TYPE['can'], TYPE['pet']],
                              None]

    def of_date(self, date):
        from math import ceil
        week_of_month = ceil(date.day / 7)
        weekday = date.weekday()

        if (week_of_month == 2 or week_of_month == 4) and (weekday == 3):
            sp_schedule = self.BASE_SCHEDULE[weekday].copy()
            sp_schedule.append(TYPE['used_paper'])
            sp_schedule.append(TYPE['cloth'])
            return sp_schedule
        else:
            return self.BASE_SCHEDULE[weekday]

    def of_weekday(self, weekday):
        return self.SCHEDULE[weekday]
