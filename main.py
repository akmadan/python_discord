import discord 
import tokens   # secrets is a python file that contains bot token
client = discord.Client() 

token = tokens.TOKEN

@client.event 
async def on_message(message): 
    msg = message.content.lower() 
    if(message.author == client.user):
        return 
    else: 
        
        if(msg.startswith('hello') or (msg.startswith('hi'))): 
            await message.channel.send('Hi! '+str(message.author)+'!')

client.run(token)