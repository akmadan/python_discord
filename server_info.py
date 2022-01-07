import discord 
from discord.ext import commands 
import tokens

client = commands.Bot(command_prefix='/') 

@client.command() 
async def server(ctx): 
    name = str(ctx.guild.name )
    description = str(ctx.guild.description )
    owner = str(ctx.guild.owner )
    region = str(ctx.guild.region )
    id = str(ctx.guild.id )
    icon = str(ctx.guild.icon_url )
    members = str(ctx.guild.member_count )

    embed  = discord.Embed( 
        title = name ,
        description  = description ,
        color = discord.Color.blue()
    )
    
    embed.set_thumbnail(url = icon) 
    embed.add_field(name = "Owner Info", value = owner, inline = True)
    embed.add_field(name = "Server ID", value = id, inline = True)
    embed.add_field(name = "Region", value= region, inline=True)
    embed.add_field(name = "Member Count", value = members, inline = True)

    await ctx.send(embed = embed)

client.run(tokens.TOKEN) 


