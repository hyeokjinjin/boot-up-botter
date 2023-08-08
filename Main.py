import responses
import discord

async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)
        
    except Exception as e:
        print(e)


def runBot():
    TOKEN = 'MTEzODI4MDg4MTgwMzUwOTc2MA.GN-8HT.aVVyGKQiF4lXi9JkWYis_j4mDAakXlbei_NLZc'
    client = discord.Client(intents = discord.Intents.all())   

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} said: '{user_message}' in {channel}")
        
        if user_message[0] == '$':
            user_message = user_message[1:]
            await send_message(message, user_message)
    
        
    client.run(TOKEN)
    
runBot()