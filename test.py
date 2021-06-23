import discord
import asyncio
import datetime
import youtube_dl
import difflib

client = discord.Client()

token = "ODU2ODQwMTY3MDU3NjUzODAx.YNG4lw.XGSnAFPrSA7XyD0SE6RbU7jjHok"

@client.event
async def on_ready():

    print('Tomato가 잘 익었어요!')
    print(client.user.name)
    print('=====================')
    game = discord.Game('저에게 DM 혹은 채널에서 Tomato라고 말해보세요!')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "Tomato":
        await message.channel.send("네, 애기오빠님 무슨 일이신가요 ?\n귀엽고 사랑스러운 아타시의 애교가 보고싶으신건가요 ?!")

    if message.content == "애기오빠":
        embed = discord.Embed(color=0xA0FBFF)
        embed = discord.Embed(title="아래랑 같은 말을 외치면 제가 소환되요!", color=0xA0FBFF)
        embed.add_field(name="애기오빠 1,2", value="애기오빠님의 명언을 들을수있어요 ㅋㅋ", inline=False)
        embed.add_field(name="오빠야 내 핑 어떠노?", value="핑을 알려드려요", inline=False)
        embed.add_field(name="야 내정보", value="님 정보 알려드려요", inline=False)
        embed.add_field(name="블라이스/로아/섹스/호우/두부", value="이스타에그", inline=False)
        embed.add_field(name="야 들어와 / 어 나가 저리 꺼져", value="제가 외롭지 않게 보이스를 입/퇴장 해줘요!", inline=False)
        embed.add_field(name="불러봐", value="만들어야하는데 귀찮아!", inline=False)
        embed.add_field(name="오빠 전달해줘 <아이디> <내용>", value="개인DM으로 전달해줘요!", inline=False)
        embed.add_field(name="없애 <숫자>", value="채팅이 밀려요!", inline=False)
        embed.add_field(name="알려라 <내용>", value="그 자리에 공지문을 써줘요", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/839881607060914256/852219919060041809/ezgif-4-9dd9b8211bd3.gif")
        embed.set_footer(text="제 임배드의 색깔은 제 퍼스날 칼라에요!", icon_url="https://cdn.discordapp.com/attachments/839881607060914256/852219921886478356/ezgif-7-f79e32e18689.gif")
        await message.channel.send("{}".format(message.author.mention), embed=embed)

    # 애기오빠 1,2
    if message.content == "애기오빠 1":
        embed = discord.Embed(title="애기오빠님의 명언 중 하나에요!", description="자드야 믿고있어서 역시 너는 나에 짱친이다\n귀여운 동생들아 고마워 소예 김환 신예 너네도 고마워\n――――――――――――――――――――――――――――", color=0xA0FBFF)
        embed.set_footer(text="정말 좋은 명언이라 생각되요 !", icon_url="https://cdn.discordapp.com/attachments/839881607060914256/852219921886478356/ezgif-7-f79e32e18689.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/839881607060914256/852219919503196180/ezgif-7-e98924ff2950.gif")
        await message.channel.send(embed=embed)

    if message.content == "애기오빠 2":
        embed = discord.Embed(title="애기오빠님의 명언 중 하나에요!", description="사랑해 애기오빠 내가 다 잘못했어 하.. 내가 미안해\n자기야 다시 시작하자 우리 잘 할수있어 대답 한번만 해줘 오빠 제발...\n――――――――――――――――――――――――――――", color=0xA0FBFF)
        embed.set_footer(text="정말 좋은 명언이라 생각되요 !", icon_url="https://cdn.discordapp.com/attachments/839881607060914256/852219921886478356/ezgif-7-f79e32e18689.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/839881607060914256/852219919503196180/ezgif-7-e98924ff2950.gif")
        await message.channel.send(embed=embed)

    # 이스터에그
    if message.content == "로아":
        await message.channel.send("이스터에그를 찾으셨군요..\n보상은 제 애교입니다 뿌잉뿌잉!")

    if message.content == "호우":
        await message.channel.send("호-우!")
    
    if message.content == "섹스":
        await message.channel.send("아 ㅋㅋ 야스는 인정이지\n너는 못하자나 ㅋㅋ")
        await message.channel.send("https://cdn.discordapp.com/attachments/839881607060914256/852219918825029672/ezgif-7-6308f3fad364.gif")
    
    if message.content == "블라이스":
        await message.channel.send("네? 저희 **애기오빠**님은 무슨일로 부르시나요?\n하핫!")
    
    if message.content == "두부":
        await message.channel.send("{} 야!\n {} 얘가 너 옥상으로 따라오래..".format("<@839075238574293032>", message.author.mention))

    # 명령어
    if message.content == "오빠야 내 핑 어떠노?":
        la = client.latency
        await message.channel.send(f'🏓퐁핑팡! `{str(round(la * 1000))}ms`입니당!')

    if message.content.startswith("야 내정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0xA0FBFF)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버 별명", value=message.author.display_name, inline=True)
        embed.add_field(name="멘션", value=message.author.mention, inline=True)
        embed.add_field(name="서버 가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일" , inline=True)
        embed.add_field(name="ID", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text="소중한 주인님의 기본 정보에요 !", icon_url="https://cdn.discordapp.com/attachments/839881607060914256/852219921886478356/ezgif-7-f79e32e18689.gif")
        await message.channel.send(embed=embed)

    if message.content.startswith("오빠 전달해줘"):
        author = message.guild.get_member(int(message.content[8:26]))
        msg = message.content[27:]
        await message.author.send(msg)

    if message.content.startswith ("없애"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[3:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 안내", description="최근 {}명이\n주인 {}님의 명령으로 인해 제거되었습니다\n\n――――――――――――――――――――――――――――".format(amount, message.author), color=0xA0FBFF)
            embed.set_footer(text="말끔하게 밀렸어요 !", icon_url="https://cdn.discordapp.com/attachments/839881607060914256/852219921886478356/ezgif-7-f79e32e18689.gif")
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 저에게 명령할 수 있는 권한이 없어요! 미개한 녀석!".format(message.author.mention))

    if message.content.startswith ("알려라"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            embed = discord.Embed(title="**우리 주인님의 명령이다!**", description="\n{}\n\n――――――――――――――――――――――――――――".format(notice), color=0xA0FBFF)
            embed.set_footer(text="공지한 주인님 : {}".format(message.author), icon_url="https://cdn.discordapp.com/attachments/839881607060914256/852219921886478356/ezgif-7-f79e32e18689.gif")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/839881607060914256/852219919060041809/ezgif-4-9dd9b8211bd3.gif")
            await message.channel.send ("@everyone", embed=embed)
 
        if i is False:
            await message.channel.send("{}, 당신은 저에게 공포문을 올려라 명령할 수 있는 권한이 없어요! 미개한 녀석!".format(message.author.mention))

    # 보이스관련
    if message.content.startswith("야 들어와"):
        await message.author.voice.channel.connect()
        await message.channel.send("네.. 들어갈게요..")

    if message.content.startswith("어 나가 저리 꺼져"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
        
        await voice.disconnect()
        await message.channel.send("네.. 안녕히계세요..")
        
    if message.content.startswith("불러봐"):
        for vc in client.voice_clients:
          if vc.guild == message.guild:
                voice = vc
        
        url = message.content.split(" ")[1]
        option = {
            'outtmpl' : "file/" + url.split('-')[1] + ".mp3" 
        }
        with youtube_dl.YoutubeDL(option) as ydl:

            ydl.download([url])
            info = ydl.extract_info(url, download=False)
            title = info["title"]
        voice.play(discord.FFmpegPCMAudio("file/" + url.split('-')[1] + ".mp3"))
        await message.content.send(title + "(을)를 불러볼게요!")
   
client.run(token)