import discord
from bot_token import * # import secret file

 # defining intents
intents = discord.Intents.default()
intents.members = True

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
    await channel.send(f'Hello, {user.mention}!')


# Run the bot
client.run(token)

print("hello")
