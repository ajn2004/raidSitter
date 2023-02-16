import discord
from bot_token import * # import secret file

 # defining intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents = intents)

# Set the user to monitor
WATCHED_USER = Balton # dis is for deego


# Event that is triggered when the bot is ready
@client.event
async def on_ready():
    print('bot is ready')

    # Find the exampleServer server
    server = discord.utils.get(client.guilds, name="Presynaptic")
    if server is None:
        print("Server not found")
        return

    # Find the example-channel channel in the server
    channel = discord.utils.get(server.channels, name="bots")
    if channel is None:
        print("Channel not found")
        return
    user = client.get_user(WATCHED_USER)
    if user is None:
        print("User not found")
        return
    # Send the message to the channel
    # await channel.send(f'Hello I am the bot!, {user.mention}!')
    # Now I think we will want to have the bot scrape all previous messages from Deego in bench-list
    channel = discord.utils.get(server.channels, name="bench-lists")
    if channel is None:
        print("Couldn't connect to #bench-list")
        return
    # here we are in bench lists
    messages = [message async for message in channel.history(limit=200)]
    for msg in messages:
        if(msg.author.id == Deego):
            print(msg.content)

# On message functionality to respond to messages in the appropriate channel from the appropriate user
@client.event
async def on_message(message):
    if message.channel.name == "bots":
        if message.author.id == Balton:
            user = client.get_user(Balton)
            print(message.content)
            await message.channel.send(f"Hey {user.mention}, did you say '{message.content}'?")
        
# Run the bot
client.run(token)

print("hello")
