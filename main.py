import discord 
import tokens 


client = discord.Client()  

token = tokens.TOKEN

@client.event
async def on_message(message):
    msg = message.content.lower() 
    if(message.author == client.user):
        return 
    else: 
        ## greet back the user
        if(msg.startswith('hello') or msg.startswith('hi')): 
            await message.channel.send('Hi! '+str(message.author))
        
        ## delete abusive content
        if('kill' in msg or 'murder' in msg): 
            await message.channel.purge(limit = 1)

client.run(token)

