import discord 
import tokens   # secrets is a python file that contains bot token
client = discord.Client() 

token = tokens.TOKEN

@client.event 
async def on_message(message): 
    msg = message.content.lower() 


    if(message.author == client.user):  #no message if bot is only the sender
        return 
    else: 
        
        ## greet message
        if(msg.startswith('hello') or (msg.startswith('hi'))):  
            await message.channel.send('Hi! '+str(message.author)+'!')  #greet back the user


        ## delete sensitive message
        if('kill' in msg):
            await message.channel.purge(limit = 1)

client.run(token)