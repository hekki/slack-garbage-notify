from slackbot.bot import respond_to
from bot.schedule import Scedule


@respond_to(r'^.*今日.*ごみ.*$')
@respond_to(r'^.*今日.*ゴミ.*$')
def mention_func(message):
    from datetime import date
    today_weekday = date.today().weekday()

    scedule = Scedule()
    if scedule.of_weekday(today_weekday) is None:
        message.reply('今日は何も出せないよ！')
    else:
        today_scedule = ', '.join(scedule.of_weekday(today_weekday))
        message.reply(f"{'今日のゴミは' + ' *' + today_scedule + '* ' + 'だよ！'}")


@respond_to(r'^.*明日.*ごみ.*$')
@respond_to(r'^.*明日.*ゴミ.*$')
@respond_to(r'^ごみ$')
@respond_to(r'^ゴミ$')
def mention_func(message):
    from datetime import date, timedelta
    tomorrow = date.today() + timedelta(days=1)
    tomorrow_weekday = tomorrow.weekday()

    scedule = Scedule()
    if scedule.of_weekday(tomorrow_weekday) is None:
        message.reply('明日は何も出せないよ！')
    else:
        tomorrow_scedule = ', '.join(scedule.of_weekday(tomorrow_weekday))
        message.reply(f"{'明日のゴミは' + ' *' + tomorrow_scedule + '* ' + 'だよ！'}")
