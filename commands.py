import discord 
from discord.ext import commands 
import tokens
import requests
import json

client = commands.Bot(command_prefix = "/") 

@client.command() 
async def hello(ctx, *args):
    # for arg in args:
    #     await ctx.send(arg) 
    await ctx.send(ctx.author) 
    await ctx.send(ctx.message) 

@client.command()
async def numbers(ctx, arg):
    api_string = 'http://numbersapi.com/' +str(arg)+'/math'
    response = requests.get(api_string)
    print(response.text)
    await ctx.send(response.text)


    
client.run(tokens.TOKEN) 



