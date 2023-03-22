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
    print('bot is ready')

    # Find the exampleServer server
    server = discord.utils.get(client.guilds, name="Presynaptic")
    if server is None:
        print("Server not found")
        return

    # Find the example-channel channel in the server
    # channel = discord.utils.get(server.channels, id = 849871979326210069)
    channel = discord.utils.get(server.channels, name = "bots")
    if channel is None:
        print("Channel not found")
        return
    # we should have this bot alway run on a thursday
    today = datetime.today() # get today, and add in future dates
    raidDays = {}
    # raidDays["nextFri"] = today + timedelta(days=1) # 
    # raidDays["nextSat"] = today + timedelta(days=2) # pants 10 sat
    # raidDays["nextSun"] = today + timedelta(days=3) # 
    # raidDays["nextMon"] = today + timedelta(days=4) # balton 10 mon
    raidDays["nextTues"] = [today + timedelta(days=5), 'Ulduar 25'] # guild 25 tues
    # raidDays["nextWeds"] = [today + timedelta(days=6), 'Ulduar 10'] # medys 10 weds
    # raidDays["nextThur"] = [today + timedelta(days=7), 'Ulduar 25'] # guild 25 thurs
    # This appears to work largely as expected
    for day in raidDays.keys():
        schedule_command = f"/quickcreate [template: 4] [title: {raidDays[day][1]}] [description: Check pinned message for details] [date: {raidDays[day][0].strftime('%d-%m-%Y')}] [time: 19:00]"
        await channel.send(schedule_command)
    # this pings everyone
    # await channel.send("@here Weekly Signup Reminder")
    await client.logout()
    
client.run(token)

print("hello")
