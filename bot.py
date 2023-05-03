import disnake
import datetime
import setting


timetable = {
    "日曜日": "**日曜日は休み**",
    "月曜日": "**月曜日\n\n:one::数学Ⅰ\n:two::国語A\n:three::理科特論\n:four::英語\n:five::数学A\n:six::公民**",
    "火曜日": "**火曜日\n\n:one::GlobalStudy\n:two::技術\n:three::音楽\n:four::英語\n:five::英語\n:six::保健**",
    "水曜日": "**水曜日\n\n:one::LHM\n:two::理科Ⅱ\n:three::国語B\n:four::英語\n:five::国語A\n:six::体育**",
    "木曜日": "**木曜日\n\n:one::国語B\n:two::数学Ⅰ\n:three::歴史\n:four::理科Ⅰ\n:five::美術\n:six::公民**",
    "金曜日": "**金曜日\n\n:one::数学Ⅰ\n:two::理科Ⅰ\n:three::歴史\n:four::英語\n:five::理科Ⅱ\n:six::体育**",
    "土曜日": "**土曜日\n\n:one::数学A\n:two::英語\n:three::数学Ⅰ\n:four::道徳**"
}


def getTimetable(day) -> str:
    if isinstance(day, str) and day in timetable:
        return timetable[day]
    elif isinstance(day, int):
        weekday = timetable.keys()[day%7]
        return timetable[weekday]


bot: disnake.Client = disnake.Client(intents=disnake.Intents.all())


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    today = datetime.date.today()

    if  message.content == '時間割':
        response = getTimetable(today)

    elif message.content == '明日の時間割':
        response = getTimetable(today+1)

    await message.channel.send(response)


bot.run(setting.TOKEN)