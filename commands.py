import discord 
from discord.ext import commands 
import tokens 
import requests 



client = commands.Bot(command_prefix='/') 


@client.command()
async def hello(context, *args):
    for arg in args: 

        await context.send(arg)



@client.command()
async def numbers(context, arg): 
    api_string = 'http://numbersapi.com/' + str(arg) +'/math'
    response = requests.get(api_string) 
    await context.send(response.text)

client.run(tokens.TOKEN)