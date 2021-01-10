import asyncio
import random
import string
import discord
import requests

client = discord.Client()
token = 'Nzk3NzkzOTA4MDAzNDM4NjAz.X_rpeQ.Ui8reBM1j_KEZoMKKcmctT_oHfg'


@client.event
async def on_ready():
    print('on')
    stream = discord.Streaming(name="초고랭랜덤계정전문샵", url='https://www.twitch.tv/twitch')
    await client.change_presence(status=discord.Status.online, activity=stream)


@client.event
async def on_message(message):
    if message.content.startswith("&도움"):
        embed = discord.Embed(color=0x7289da)
        embed.add_field(name=":white_check_mark: 디엠으로 명령어 목록이 전달되었습니다.", value="dm을 확인해주세요.",inline=False)
        await message.channel.send(embed=embed)
        embed = discord.Embed(color=0x7289da)
        embed.add_field(name="&니트로", value="랜덤으로 니트로를 생성합니다",inline=False)
        embed.add_field(name="&문상", value="랜덤으로 문화상품권을 생성합니다",inline=False)
        embed.add_field(name="&청소", value="메시지를 청소합니다",inline=False)
        embed.add_field(name="&실검", value="실시간검색어 순위를 보여줍니다",inline=False)
        embed.add_field(name="&출근", value="관리자 권한이 있을경우 출근로그를 표시합니다",inline=False)
        embed.add_field(name="&퇴근", value="관리자 권한이 있을경우 퇴근로그를 표시합니다",inline=False)
        embed.add_field(name="&임시퇴근", value="관리자 권한이 있을경우 임시퇴근로그를 표시합니다",inline=False)
        embed.add_field(name="&휴가", value="관리자 권한이 있을경우 휴가로그를 표시합니다",inline=False)
        embed.add_field(name="&서버링크", value="서버링크를 표시합니다",inline=False)
        embed.add_field(name="&주문제작", value="주문제작 가격표를 표시합니다", inline=False)
        await message.author.send(embed=embed)

    if message.content.startswith('&니트로'):
        ranNitro = ""
        for i in range(0, 16):
            ranNitro += str(random.choice(string.ascii_letters))
            NITROembed = discord.Embed(title='🎨 니트로 생성했어용!', description='https://discord.gift/' + ranNitro,
                                       color=0x7289da)
        await message.channel.send(embed=NITROembed)

    if message.content.startswith('&문상') or message.content.startswith('&문화상품권'):
        a = random.randint(2100, 3800)
        b = random.randint(1000, 9999)
        b2 = random.randint(1000, 9999)
        c = random.randint(100000, 999999)
        TICKETembed = discord.Embed(title='💵 문화상품권을 생성했어용!',
                                    description=str(a) + '-' + str(b) + '-' + str(b2) + '-' + str(c), color=0x7289da)
        await message.channel.send(embed=TICKETembed)

    if message.content.startswith('&청소'):
        try:
            if message.author.guild_permissions.manage_messages:
                amount = message.content[4:]
                await message.delete()
                await message.channel.purge(limit=int(amount))
                message = await message.channel.send(
                    embed=discord.Embed(title='🧹 메시지 ' + str(amount) + '개 삭제됨', color=0x7289da))
                await asyncio.sleep(2)

            else:
                await message.channel.send('``명령어 사용권한이 없어요..ㅜㅜ``')
        except:
            pass

    if message.content.startswith("&출근"):
        try:
            if message.author.guild_permissions.manage_messages:
                await message.delete()
                embed = discord.Embed(color=0x7289da)
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 출근하였습니다.')
                await message.channel.send(embed=embed)
        except:
            pass

    if message.content.startswith("&퇴근"):
        try:
            if message.author.guild_permissions.manage_messages:
                await message.delete()
                embed = discord.Embed(color=0x7289da)
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 퇴근하였습니다.')
                await message.channel.send(embed=embed)
        except:
            pass

    if message.content.startswith("&임시퇴근"):
        try:
            if message.author.guild_permissions.manage_messages:
                await message.delete()
                embed = discord.Embed(color=0x7289da)
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 임시로 퇴근 하였습니다.')
                await message.channel.send(embed=embed)
        except:
            pass

    if message.content.startswith("&휴가"):
        try:
            if message.author.guild_permissions.manage_messages:
                await message.delete()
                embed = discord.Embed(color=0x7289da)
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 휴가 가셨습니다.')
                await message.channel.send(embed=embed)
        except:
            pass

    if message.content.startswith('&실시간검색어') or message.content.startswith('&실검'):
        json = requests.get('https://www.naver.com/srchrank?frm=main').json()
        ranks = json.get("data")
        data = []
        for r in ranks:
            rank = r.get("rank")
            keyword = r.get("keyword")
            if rank > 10:
                break
            data.append(f'**{rank}**위 {keyword}')

        dat = str(data)
        dat = dat.replace("'", "")
        dat = dat.replace(", ", "\n")
        dat = dat[1:-1]
        print(dat)
        embed = discord.Embed(title='네이버 실시간 검색어 순위입니다!', description=(dat), color=0x7289da)
        await message.channel.send(embed=embed)

    if message.content.startswith('&링크'):
        TEXTAembed = discord.Embed(
            title='✅ㅣ초고랭 랜덤계정샵 초대링크입니다 https://discord.gg/QpaEncj', color=0x7289da)
        await message.channel.send(embed=TEXTAembed)

    if message.content.startswith("&주문제작"):
        embed = discord.Embed(color=0x7289da)
        embed.add_field(name=":white_check_mark: 디엠으로 주문제작 목록이 전달되었습니다.", value="dm을 확인해주세요.", inline=False)
        await message.channel.send(embed=embed)
        embed = discord.Embed(color=0x7289da)
        embed.add_field(name="다이아 보장", value="탱 힐  15000 딜 20000",inline=False)
        embed.add_field(name="마스터 보장", value="탱 힐  25000 딜  35000",inline=False)
        embed.add_field(name="그랜드마스터 보장", value="탱 힐 50000 딜 60000",inline=False)
        embed.add_field(name="랭커 보장", value="관리자 문의",inline=False)

        await message.author.send(embed=embed)

    if message.content.startswith('https://discord.gg/'):
        await message.delete()
        TEXTFFAembed = discord.Embed(
            title=':x: 앞메 금지!!!:x: ', color=0x7289da)
        await message.channel.send(embed=TEXTFFAembed)

    if message.content.startswith('시발'):
        await message.delete()
        TEXTFFAembed = discord.Embed(
            title=':x:욕은 나빠!!![검열된 채팅(시발)]:x:', color=0x7289da)
        await message.channel.send(embed=TEXTFFAembed)

    if message.content.startswith('병신'):
        await message.delete()
        TEXTFFAembed = discord.Embed(
            title=':x:욕은 나빠!!![검열된 채팅(병신)]:x:', color=0x7289da)
        await message.channel.send(embed=TEXTFFAembed)

    if message.content.startswith('ㅅㅂ'):
        await message.delete()
        TEXTFFAembed = discord.Embed(
            title=':x:욕은 나빠!!![검열된 채팅(ㅅㅂ)]:x:', color=0x7289da)
        await message.channel.send(embed=TEXTFFAembed)

    if message.content.startswith('ㅂㅅ'):
        await message.delete()
        TEXTFFAembed = discord.Embed(
            title=':x:욕은 나빠!!![검열된 채팅(ㅂㅅ)]:x:', color=0x7289da)
        await message.channel.send(embed=TEXTFFAembed)

    if message.content.startswith('니애미'):
        await message.delete()
        TEXTFFAembed = discord.Embed(
            title=':x:욕은 나빠!!![검열된 채팅(니애미)]:x:', color=0x7289da)
        await message.channel.send(embed=TEXTFFAembed)

    if message.content.startswith('니애비'):
        await message.delete()
        TEXTFFAembed = discord.Embed(
            title=':x:욕은 나빠!!![검열된 채팅(니애비)]:x:', color=0x7289da)
        await message.channel.send(embed=TEXTFFAembed)

    if message.content.startswith('망고맘'):
        await message.delete()
        TEXTFFAembed = discord.Embed(
            title=':x:욕은 나빠!!![검열된 채팅(망고맘)]:x:', color=0x7289da)
        await message.channel.send(embed=TEXTFFAembed)

    if message.content.startswith('호떡맘'):
        await message.delete()
        TEXTFFAembed = discord.Embed(
            title=':x:욕은 나빠!!![검열된 채팅(호떡맘)]:x:', color=0x7289da)
        await message.channel.send(embed=TEXTFFAembed)

  

client.run(token)