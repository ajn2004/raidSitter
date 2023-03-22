import discord
from bot_token import * # import secret file
from discord.ext import commands
from datetime import datetime, timedelta

 # defining intents
intents = discord.Intents.default()
intents.message_content = True
permissions = discord.Permissions()
permissions.mention_everyone = True


client = discord.Client(intents = intents, permissions = permissions)

# Set the user to monitor
# Event that is triggered when the bot is ready
@client.event
async def on_ready():
    # print('bot is ready')

    # Find the exampleServer server
    server = discord.utils.get(client.guilds, name="Presynaptic")
    if server is None:
        print("Server not found")
        return
    channels = [1009788705902432276, 1023239799315902594]
    for ids in channels:        
        # Find the example-channel channel in the server
        channel = discord.utils.get(server.channels, id = ids)
        # channel = discord.utils.get(server.channels, name = "bots")
        if channel is None:
            print("Channel not found")
            return
        await channel.send("@here Signup Reminder!")
        # await channel.send("testing!")
    await client.close()
    
client.run(token)

# print("hello")




