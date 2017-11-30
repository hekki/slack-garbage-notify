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

    def of_weekday(self, weekday):
        return self.SCHEDULE[weekday]
