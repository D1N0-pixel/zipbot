import asyncio
import discord
from discord.ext import commands
import os
import datetime
import pytz


client = discord.Client()

# 봇 설정
game = discord.Game("&도움 | 집가고 싶어")
bot = commands.Bot(command_prefix='&',
                   status=discord.Status.online, activity=game)
bot.remove_command('help')

# 봇 시작
@bot.event
async def on_ready():
    print("봇 시작")


class time:
    year = 2020
    month = 9
    day = 29
    hour = 14
    minu = 0
    sec = 0


@bot.command(aliases=['도움', '도움말'])
async def help(ctx, command=''):
    if command == '':
        embed = discord.Embed(title=f"명령어 목록", color=0xf3bb76)
        embed.add_field(name=f"&도움,&도움말,&help",
                        value=f"지금 이거 ㅇㅇ", inline=False)
        embed.add_field(name=f"&설정,&setting",
                        value=f"집 가는 시간 설정", inline=False)
        embed.add_field(name=f"&집,&wlq,&zip,&시간",
                        value=f"집 가기까지 남은 시간 보기", inline=False)
        embed.add_field(name=f"&수능,&tnsmd",
                        value=f"수능까지 남은 시간 보기", inline=False)
        embed.add_field(name=f"&도움 [명령]", value=f"명령에 대한 도움", inline=False)
    elif command == '설정':
        embed = discord.Embed(color=0xf3bb76)
        embed.add_field(name=f"&설정 [연 월 일 (시 분 초)]",
                        value=f"집 가는 기본 시간을 설정합니다", inline=False)
    elif command == '집':
        embed = discord.Embed(color=0xf3bb76)
        embed.add_field(name=f"&집 ([연 월 일 (시 분 초)])",
                        value=f"집 가기까지 남은 시간을 보여줍니다", inline=False)
    elif command == '수능':
        embed = discord.Embed(color=0xf3bb76)
        embed.add_field(name=f"&수능",
                        value=f"우리의 수능날인 2022년 11월 17일까지 남은 시간을 보여줍니다", inline=False)
    else:
        return await ctx.send("잘못된 입력입니다")
    await ctx.send(embed=embed)


@bot.command(aliases=['설정'])
async def setting(ctx, year='0', month='0', day='0', hour='0', minu='0', sec='0'):
    if not (year.isdecimal() and month.isdecimal() and day.isdecimal() and hour.isdecimal() and minu.isdecimal() and sec.isdecimal()):
        return await ctx.send("잘못된 입력입니다")
    year = int(year)
    month = int(month)
    day = int(day)
    hour = int(hour)
    minu = int(minu)
    sec = int(sec)
    try:
        if year or month or day or hour or minu or sec:
            check = datetime.datetime(year, month, day, hour, minu, sec)
            global time
            time.year, time.month, time.day, time.hour, time.minu, time.sec = year, month, day, hour, minu, sec
            return await ctx.send("기본 시간이 성공적으로 변경되었습니다")
        else:
            return await ctx.send("바꿀 시간을 입력해주세요")
    except:
        return await ctx.send("잘못된 입력입니다")


@bot.command(aliases=['집', 'zip', '시간'])
async def wlq(ctx, year='0', month='0', day='0', hour='0', minu='0', sec='0'):
    if not (year.isdecimal() and month.isdecimal() and day.isdecimal() and minu.isdecimal() and sec.isdecimal()):
        return await ctx.send("잘못된 입력입니다")
    year = int(year)
    month = int(month)
    day = int(day)
    hour = int(hour)
    minu = int(minu)
    sec = int(sec)
    if not (year or month or day or hour or minu or sec):
        global time
        year, month, day, hour, minu, sec = time.year, time.month, time.day, time.hour, time.minu, time.sec
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    try:
        dday = datetime.datetime(year, month, day, hour, minu, sec)
        left_time = dday - now
        result = f"{left_time.days}일\n{int(left_time.total_seconds()//3600)}시간\n{int(left_time.total_seconds()//60)}분\n{left_time.total_seconds()}초"
        return await ctx.send(result)
    except:
        return await ctx.send("잘못된 입력입니다")


@bot.command(aliases=['수능'])
async def tnsmd(ctx):
    dday = datetime.datetime(2022, 11, 17)
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    left_time = dday - now
    result = f"{left_time.days}일\n{int(left_time.total_seconds()//3600)}시간\n{int(left_time.total_seconds()//60)}분\n{left_time.total_seconds()}초"
    return await ctx.send(result)


bot.run(os.environ['token'])
