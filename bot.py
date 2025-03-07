import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='#', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hi(ctx):
    await ctx.send(f'Hi, I am {bot.user}!')
@bot.command()
async def money(ctx, present: int, interest: float):
    future = present / (1 + interest)
    await ctx.send(f'The present value is {present} and the interest is {interest} so the future value is {future}.')
    if future == 0:
        await ctx.send(f"This number doesn't work, try other numbers")
@bot.command()
async def decimals(ctx, num1: float, num2: float):
    resultado = num1 + num2
    await ctx.send(f'El resultado de sumar {num1} y {num2} es {resultado}.')
@bot.command()
async def XD(ctx, count_xd = 5):
    if count_xd <= 10:
        await ctx.send("XD " * count_xd)
    else:
        await ctx.send(f"This number doesn't work, please choose a smaller than the previous one ")
@bot.command()
async def helping(ctx):
    await ctx.send(f"#money: means you can use the formula to find the FV for every number; #hi: the robot says Hi; #XD: Repeat certain times the word XD (10 times MAX); #decimals: The robot add two decimal numbers")
@bot.command()
async def trying(ctx):
    codes = "#XD","#decimals","#helping","#decimals","#hi"
    if codes != ctx:
        print(f"This command doesn't work, if you want help write #helping")
bot.run("Token")
