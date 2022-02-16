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

@client.command()
async def l(ctx):
    await ctx.send("Retard")
    
    @client.command()
    async def swat(ctx, member):
        await ctx.send(f"{member} just commited fraud :^)")

client.run(token, bot=False)
