import disnake


timetable = {"日曜日":"**日曜日は休み**",
             "月曜日":"**月曜日\n\n:one::数学Ⅰ\n:two::国語A\n:three::理科持論\n:four::英語\n:five::数学A\n:six::公民**",
             "火曜日":"**火曜日\n\n:one::GlobalStudy\n:two::技術\n:three::音楽\n:four::英語\n:five::英語\n:six::保健**",
             "水曜日": "**水曜日\n\n:one::LHM\n:two::理科Ⅱ\n:three::国語B\n:four::英語\n:five::国語A\n:six::体育**",
             "木曜日": "**木曜日\n\n:one::国語B\n:two::数学Ⅰ\n:three::歴史\n:four::理科Ⅰ\n:five::美術\n:six::公民**",
             "金曜日": "**金曜日\n\n:one::数学Ⅰ\n:two::理科Ⅰ\n:three::歴史\n:four::英語\n:five::理科Ⅱ\n:six::体育**",
             "土曜日": "**土曜日\n\n:one::数学A\n:two::英語\n:three::数学Ⅰ\n:four::道徳**"}

class MyClient(disnake.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'こんにちは' in message.content:
        response = 'こんにちは！'
    elif 'おはよう' in message.content:
        response = 'おはようございます！'
    else:
        response = 'よろしくお願いします！'

    await message.channel.send(response)

client = MyClient()
client.run('OTczOTI5NjE4Mjc5MTA0NTI0.GRJdHe.IbhkjySP_z6jbJS9MU6gX0VDJUhrrzYE-V0HRQ')