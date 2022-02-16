import discord
from discord.ext import commands 

client = commands.Bot (command_prefix=".", self_bot=True, help_command=None)
token = "insert_token_here"

Output = "[Output] | "

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
       pay load = {'house_id': 3}
    
    
    
              try:
                  request.posT('https://discordapp.com/api/v6/hypersquad/online, headers=headers, json=payload')
                  print(f"(Output)Successfully Set your hypersquad to (house)")
                  except:
                      print(f"(Output)Failed to set your hypersquad house.")
           
           
client.run(token, bot=False)
