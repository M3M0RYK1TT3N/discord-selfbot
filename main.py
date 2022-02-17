import discord
from discord.ext import commands
from discord import ext
from discord.ext import tasks
import ctx
from discord import Permissions, channel, message, guild
import random
import house


client = commands.Bot (command_prefix=".", self_bot=True, help_command=None)
token = ""

Output = "[Output] | "

@client.command()
async def delete(ctx,amount=1):
  await ctx.channel.purge(limit=amount+5)

@client.event
async def on_ready():
    print("Online!")
    print("Welcome to nana-bot discord-selfbot")
    print("We are currently under development")
    print("For more information please visit our github!")
    print("nana-bot selfbot version 1.0")


@commands.has_permissions(administrator=True)
async def function(ctx, prefix):
  pass

# bypasses discords api if you are banned ( ͡° ͜ʖ ͡°) 
@client.command()
async def helloworld(resp):
    if resp.event.ready_supplemental: 
        user = client.command.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
    if resp.event.message:
        m = resp.parsed.auto()
        guildID = m['guild_id'] if 'guild_id' in m else None 
        channelID = m['channel_id']
        username = m['author']['username']
        discriminator = m['author']['discriminator']
        content = m['content']
        print("> guild {} channel {} | {}#{}: {}".format(guildID, channelID, username, discriminator, content))
        

@client.command(pass_context= True)
async def ban(ctx):
  server = ctx.message.server
  member = ctx.message.author
  print(member)

@client.command()
async def a(ctx):
    await ctx.send("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


@client.command(name='spam', help='Spams the input message for x number of times')
async def spam(ctx, amount:int, *, message):
    for i in range(amount): # Do the next thing amount times
        await ctx.send(message) # Sends message where command was called



@client.command()
async def TEST(ctx):
    await ctx.send("Hello")

@client.command()
async def l(ctx):
    await ctx.send("Retard")
    
@client.command()
async def swat(ctx, member):
    await ctx.send(f"{member} just commited fraud :^)")
        
@client.command()
async def embed(ctx, title, *, description):
  await ctx.message.delete()
  embed=discord.Embed(title=title, description=description)
  await ctx.send(embed=embed)
        
@client.command()
async def acsii(ctx, *, args):
    await ctx.message.delete()
    text = pyfiglet_format(args)
    await ctx.send(f'```(text)```')
    
@client.command 
async def request(ctx):
    r = request.get('https://google.com')
    print(r.status_code)
    
@client.command
async def hypersquad(ctx, house):
    await ctx.message.delete()
    request = request.session()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
        
    }
   
if house == "bravery":
       payload = {'house_id': 1}
elif house == "brilliance":
       payload = {'house_id': 2}
elif house == "balance":
       payload = {'house_id': 3}


try:
    request.post('https://discordapp.com/api/v6/hypersquad/online, headers=headers, json=payload')
    print(f"(Output)Successfully Set your hypersquad to (house)")
except:
    print(f"(Output)Failed to set your hypersquad house.")       
    
    
    
              
              
                  
           
client.run(token, bot=False)
