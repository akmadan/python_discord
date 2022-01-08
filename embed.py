import discord 
from discord.ext import commands 
import tokens 

intents = discord.Intents.default()
intents.members = True 
client = commands.Bot(command_prefix='/', intents = intents)  

@client.command() 
async def info(context):
    server_name = str(context.guild.name) 
    description = str(context.guild.description) 
    owner_name = str(context.guild.owner) 
    id = str(context.guild.id) 
    icon = str(context.guild.icon_url) 
    members = str(context.guild.member_count) 

    embed = discord.Embed(
        title = server_name, 
        description = description, 
        color = discord.Color.dark_green() 
    )

    embed.set_thumbnail(url = icon) 
    embed.add_field(name="Owner Name", value=owner_name, inline = True) 
    embed.add_field(name="ID", value=id, inline = True) 
    embed.add_field(name="Member Count", value=members, inline = True)

    await context.send(embed = embed)

client.run(tokens.TOKEN)
