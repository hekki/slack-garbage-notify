from slackbot.bot import respond_to
from bot.schedule import Scedule


@respond_to('ゴミ|ごみ')
def mention_func(message):
    from datetime import date, datetime
    tomorrow_weekday = datetime.today().weekday() + 1

    scedule = Scedule()
    if scedule.of_weekday(tomorrow_weekday) is None:
        message.reply('明日は何も出せないよ！')
    else:
        tomorrow_scedule = ', '.join(scedule.of_weekday(tomorrow_weekday))
        message.reply(f"{'明日のゴミは' + ' *' + tomorrow_scedule + '* ' + 'だよ！'}")
