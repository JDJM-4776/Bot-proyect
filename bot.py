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
async def decimal(ctx, num1: float, num2: float):
    resultado = num1 + num2
    await ctx.send(f'El resultado de sumar {num1} y {num2} es {resultado}.')

@bot.command()
async def XD(ctx, count_xd = 5):
    await ctx.send("XD" * count_xd)

bot.run("%")
