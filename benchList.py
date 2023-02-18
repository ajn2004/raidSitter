# this file should contain the relevant code for handling the bench-list channel
# in the Guilds discord
# We are assuming 1 officer is responsible for keeping track of the offical bench-list
# The bench list will be reported as
# month-day '10/25'm:
# <@player1DiscordNumber>
# <@player2DiscordNumber>
# ...
# <@playerNDiscordNumber>

from bot_token import Deego # Here we identify Deego as the log-keeper

async def getChannelMessages(channel, user = Deego, limit = None):
    
    # Input:
    #               channel: discord channel object, passed from main.py 
    #   discordPlayerNumber: Integer idetifying a player
    #                 limit: optional limit for number of messages returned
    # Output:
    #   list of strings of desired messages
    #
    # Description:
    #   Basic function to return a list of messages from a specified channel/user combination
    if limit:
        return [message.content async for message in channel.history(limit = limit) if message.author.id == user]
    return [message.content async for message in channel.history() if message.author.id == user]
    
def writeBenchListToFile(messages, user = Deego, fileName = 'presynaptic_db'):
    # Input:
    #   messages: a list of messages from getChannelmessages
    #       user: discordplayernumber defaulted to Deego
    #   fileName: a string to specify the file that will be written
    # Output:
    #   None
    # Description:
    #   Function takes in a list of messages and writes them to a text file for future use
    with open(fileName,'w+') as f:
        for msg in messages:
            try: # check to make sure we're looking at a date
                isaDate = int(msg[0])
                f.write(msg)
                f.write('\n')
            except:
                pass
        f.close()

def cleanPlayerList(playerList):
    # Inputs:
    #  playerList: a list of player discord numbers in string type from a channel message object
    # Output:
    #   cleanList: a list of player discord numbers in int type
    return [int(player.replace('<@','').replace('>','').replace(' ','')) for player in playerList]
     
def parseBenchMessage(message):
    # Inputs:
    #   message: formatted string to be parsed
    # Output:
    #   parseResults: a dict containing the parsed information from message
    # function to parse bench list log messages
    parseResults = {}
    lines = message.split('\n') # grab the lines of the message individually
    # date is contained in the first line, we assume a proper message at this point
    parseResults['date'] = {'month': int(lines[0].split(' ')[0].split('-')[0]),
                            'day': int(lines[0].split(' ')[0].split('-')[1])}
    parseResults['difficulty'] = int(lines[0][-4:-2])
    print(lines[1:])
    parseResults['players'] = cleanPlayerList(lines[1:])
    return parseResults

def buildSitLog(messages):
    # Inputs:
    #   messages: list of formatted string to be parsed
    # Output:
    #   parseResults: a dict containing the parsed information from message
    # Build a list of parse objects containing relevant sit information
    raidSitLog = []
    for msg in messages:
        try:
            num = int(msg[0])
            # print(msg)
            raidSitLog.append(parseBenchMessage(msg))
            # print(raidSitLog)
        except:
            pass
    return raidSitLog

async def manageBenchLists(channel, user = Deego, fileName = 'presynaptic_db', limit = None):
    # Inputs:
    #   channel: discord channel object
    #      user: discord player number defaulted to Deego
    #  fileName: string representing file name to write channel data to
    #     limit: number of messages to limit the scope to
    messages = await getChannelMessages(channel, user = user, limit = limit)
    raidSitLog = buildSitLog(messages)
    for log in raidSitLog:
        print(log)
        print('\n')
