from slackbot.bot import respond_to
from bot.schedule import Scedule


@respond_to(r'^ごみ$')
@respond_to(r'^ゴミ$')
def mention_func(message):
    from datetime import date

    scedule = Scedule()
    if scedule.of_date(date.today()) is None:
        message.reply('今日は何も出せないよ！')
    else:
        today_scedule = ', '.join(scedule.of_date(date.today()))
        message.reply(f"{'今日のゴミは' + ' *' + today_scedule + '* ' + 'だよ！'}")


@respond_to(r'^.*明日.*$')
def mention_func(message):
    from datetime import date, timedelta
    tomorrow = date.today() + timedelta(days=1)

    scedule = Scedule()
    if scedule.of_date(tomorrow) is None:
        message.reply('明日は何も出せないよ！')
    else:
        tomorrow_scedule = ', '.join(scedule.of_date(tomorrow))
        message.reply(f"{'明日のゴミは' + ' *' + tomorrow_scedule + '* ' + 'だよ！'}")
