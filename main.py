import discord
from discord.ext import commands 

client = commands.Bot (command_prefix=".", self_bot=True, help_command=None)
token = "insert_token_here"

@client.event
async def on_ready():
    print("Online!")

@client.command()
async def TEST(ctx):
    await ctx.send("Hello")

client.run(token, bot=False)
