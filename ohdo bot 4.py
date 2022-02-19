import discord
import random

client = discord.Client()

token = "OTAzMjkwMDMwMTMzNTEwMjQ0.YXq0ZQ.wTvgjeQrZja3fKTWX1OCfn5cwHo"

#bad = ["ㅅㅂ", "시발", "tlqkf", "병신", "ㅂㅅ", "ㅄ", "qudtls", "씨발", "시바", "좆", "ㅈ같네", "시이발", "섹스", "ㅅㅅ", "섻으", "시.발", "병.신", "지랄", "ㅈㄹ", "지.랄", "ㅗ", "ㅅ.ㅂ", "ㅂ.ㅅ", "ㅈ.ㄹ", "개새끼"]

@client.event
async def on_ready():
    print(client.user.name)
    print("준비_완료")
    game = discord.Game("서버 감시")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    global doing
    if message.author.id == client.user.id:
        return
    if message.content == "백호":
        await message.channel.send("일해라 준법위 이사장아 짜르기전에")

    if message.content == "헬퍼":
        await message.channel.send("뭐하냐")

    if message.content == "!오도봇":
        await message.channel.send(f"{message.author.mention} 나 불렀어?")

    if message.content == "독재자":
        await message.channel.send(f"{message.author.mention} 너 적폐. 미아보호소 가고 싶어?")

    if message.content == "오도":
        await message.channel.send("위대한 이사장님... 오도!")

    mc = message.content

    # for i in bad:
    # if i in mc:
    # await message.channel.send(f"{message.author.mention} 새끼야 너 자꾸그러면 -찢- 한다?")
    # await message.delete()

    if message.content.startswith("!청소"):
        number = int(message.content.split()[1])
        await message.channel.purge(limit=number + 1)
        await message.channel.send(f"{number}개 메세지 청소 완료 ✅")

    if message.content == "!가위" or message.content == "!바위" or message.content == "!보":
        bot_response = random.randint(1, 3)
        if bot_response == 1:
            if message.content == "!가위":
                await message.channel.send("가위 / 비겼어 다시해!")
            elif message.content == "!바위":
                await message.channel.send("가위 / 내가 졌어 ㅠ...")
            elif message.content == "!보":
                await message.channel.send("가위 / 내가 이김 ㅎㅎ 봇한테도 지는 인간... ㅉㅉ")
        elif bot_response == 2:
            if message.content == "!가위":
                await message.channel.send("바위 / 내가 이겼다 ㅋㅋㅋ")
            elif message.content == "!바위":
                await message.channel.send("바위 / 이걸 비기네?")
            elif message.content == "!보":
                await message.channel.send("바위 / 내가 졌지만 내가 이긴걸로 하자 ㅎㅎ")
        elif bot_response == 3:
            if message.content == "!가위":
                await message.channel.send("보 / 내가 졌어...?!?!")
            elif message.content == "!바위":
                await message.channel.send("보 / 역시 나야. 내가 이겼어 ㅎㅎ")
            elif message.content == "!보":
                await message.channel.send("보 / 비겼어... 이게 말이되나?")

    wt = ["몰라", "놀고 있을듯?", "사냥 나갔데", "어흥 한데", "코딩중이래", "파업 시위한데", "귀찮데", "이사장 엿먹으래", "용용이가 싫데", "반달러가 되겠다고 다짐했데", "ㅇㅅㅇ", "직접 물어봐달래", "강주야 얼불춤 좀 그만하래", "응애"]
    if message.content.startswith('!백호는'):
        doing = random.choice(wt)
        await message.channel.send(f"최첨단 인공지능 오도봇 1.0을 활용해 추측한 결과... {doing}")

    if message.content == "!도움":
        embed = discord.Embed(title="도움말", description="Ohdo bot 4에 대한 도움말입니다.", color=0x62c1cc)
        embed.add_field(name="백호는", value="``!백호는``을 입력하시면 백호랜드의 마스코트이자 준법위 초대 위원장인 백호가 오늘 지금 상태인지 최첨단 인공지능 오도봇 1.0을 통해 알려드립니다!", inline=False)
        embed.add_field(name="가위바위보", value="``!가위``와 같은 형식으로 입력하시면 바로 게임이 진행됩니다. ", inline=False)
        embed.add_field(name="기타", value="특정 단어들을 말하면 재미있는 대답을 받으실 수 있습니다.", inline=False)
        await message.channel.send(embed=embed)

client.run(token)