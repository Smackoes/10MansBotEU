#10 Mans Bot EU by Smackoes
#15/01/2019
#Version 4.00 Released

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

"""GAME DISPLAYED"""

#GameStatus = "Down for Maintenance"
GameStatus = "!commands for help | S4"


"""---------------------CODE-----------------------"""

bot = commands.Bot(command_prefix='!')

"""ANY CHANGES REQUIRE REBOOT OF FILE"""

@bot.event
async def on_ready():
    print ("Ready!")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name=GameStatus, type=0)) 
    #await bot.change_presence(game=discord.Game(name=GameStatus, type=1, url='https://www.twitch.tv/janisarry'))   
    #await bot.change_presence(game=discord.Game(name=GameStatus, type=2))
    #await bot.change_presence(game=discord.Game(name=GameStatus, type=3))

    """type=0=playing, type=1=streaming, type=2=listening, type=3=watching"""


"""BATTLE BOT"""

ge = discord.Embed()
ge.set_image(url="https://d1u5p3l4wpay3k.cloudfront.net/heroesandgenerals_gamepedia/3/3e/Icon-GR-Symbol.png?version=a27b3cf3addb1635ee9c99e4a37ee1ac")

us = discord.Embed()
us.set_image(url="https://d1u5p3l4wpay3k.cloudfront.net/heroesandgenerals_gamepedia/8/83/Icon-US-Symbol.png?version=312400bbecd4db68cf1d8d4ba0859e01")

su = discord.Embed()
su.set_image(url="https://d1u5p3l4wpay3k.cloudfront.net/heroesandgenerals_gamepedia/9/9c/Icon-SU-Symbol.png?version=3681e1d0059fac8e159f7acab615e66f")

"""ARRAYS"""

queuege = []
queueus = []
queuesu = []

"""ARRAY CHECKS"""

def EnquiryGE(queuege): 
    if len(queuege) == 0: 
        return 0
    else: 
        return 1

def queuegeComplete(queuege): 
    if len(queuege) == 5: 
        return 1
    else: 
        return 0

queueus = []
def EnquiryUS(queueus): 
    if len(queueus) == 0: 
        return 0
    else: 
        return 1

def queueusComplete(queueus): 
    if len(queueus) == 5: 
        return 1
    else: 
        return 0

queueus = []
def EnquirySU(queuesu): 
    if len(queuesu) == 0: 
        return 0
    else: 
        return 1

def queuesuComplete(queuesu): 
    if len(queuesu) == 5: 
        return 1
    else: 
        return 0


@bot.event
async def on_message(message):

    """DEFINE"""

    gecount = str(len(queuege))
    uscount = str(len(queueus))
    sucount = str(len(queuesu))

    """COMMANDS"""

    if message.content.lower().startswith('!commands'):
        await bot.send_message(message.channel, "fc = us/ge/su\n\n!q fc - To Queue for a faction\n!remove fc - To remove yourself from the Queue\n!status - To check the Queues\n!clear fc - To clear a factions Queue (Admin)\n!clear all- To clear all Queues (Admin)")

    """CORRECTIONS"""

    if message.content.lower().startswith('!q fc'):
        await bot.send_message(message.channel, "fc = ge, us or su")

    if message.content.lower().startswith('!remove fc'):
        await bot.send_message(message.channel, "fc (faction) = ge, us or su")

    if message.content.lower().startswith('!qe'):
        await bot.send_message(message.channel, "Use !q ge, us or su")

    if message.content.lower().startswith('!leave'):
        await bot.send_message(message.channel, "Use !remove ge, us or su")

    if message.content.lower().startswith('?join'):
        await bot.send_message(message.channel, "Use ?rank ge, us or su")

    """QUEUES"""
    """GE QUEUE"""

    if message.content.lower().startswith('!q ge'):
        """message"""
        userID = message.author.id
        user = message.author
        """action"""
        if user in queuege :
            print("Yes, 'at' found in List : " , queuege)
            await bot.send_message(message.channel, "<@%s> You are already in the German queue!" % (userID))
        elif user in queueus:
            print("Yes, 'at' found in List : " , queueus)
            await bot.send_message(message.channel, "<@%s> You are already in the US queue!" % (userID))
        elif user in queuesu:
            print("Yes, 'at' found in List : " , queuesu)
            await bot.send_message(message.channel, "<@%s> You are already in the SU queue!" % (userID))
        else:
            await bot.send_message(message.channel, "<@%s> You are now queued for Germany!" % (userID))
            queuege.append(user)
            print(queuege)

            if queuegeComplete(queuege):
                separator = ", "
                await bot.send_message(message.channel, "Full German queue!")
                """Check US and SU Queue"""
                if len(queuege) <= len(queueus):
                    await bot.send_message(message.channel, "Battle Ready!\n" + gecount + " GE: " + separator.join([user.mention for user in queuege]) + "\n" + uscount + " US: " + separator.join([user.mention for user in queueus]) + "\nPlease join the 'Decide the City' voice room to get your battle going! Once all 5 members from each faction join you are ready to pop a war battle!")
                    await bot.send_message(message.channel, embed=ge)
                    await bot.send_message(message.channel, embed=us)
                if len(queuege) <= len(queuesu):
                    await bot.send_message(message.channel, "Battle Ready!\n" + gecount + " GE: " + separator.join([user.mention for user in queuege]) + "\n" + sucount + " SU: " + separator.join([user.mention for user in queuesu]) + "\nPlease join the 'Decide the City' voice room to get your battle going! Once all 5 members from each faction join you are ready to pop a war battle!")
                    await bot.send_message(message.channel, embed=ge)
                    await bot.send_message(message.channel, embed=su)

    if message.content.lower().startswith('!remove ge'):
        """message"""
        userID = message.author.id
        user = message.author
        await bot.send_message(message.channel, "<@%s> Removed from queue!" % (userID))
        """action"""
        queuege.remove(user)
    

    """US QUEUE"""

    if message.content.lower().startswith('!q us'):
        """message"""
        userID = message.author.id
        user = message.author
        """action"""
        if user in queuege:
            print("Yes, 'at' found in List : " , queuege)
            await bot.send_message(message.channel, "<@%s> You are already in the German queue!" % (userID))
        elif user in queueus:
            print("Yes, 'at' found in List : " , queueus)
            await bot.send_message(message.channel, "<@%s> You are already in the US queue!" % (userID))
        elif user in queuesu:
            print("Yes, 'at' found in List : " , queuesu)
            await bot.send_message(message.channel, "<@%s> You are already in the SU queue!" % (userID))
        else:
            await bot.send_message(message.channel, "<@%s> You are now queued for the United States!" % (userID))
            queueus.append(user)
            print(queueus)

            if queueusComplete(queueus):
                separator = ", "
                await bot.send_message(message.channel, "Full US queue!")
                """Check GE and SU Queue"""
                if len(queueus) <= len(queuege):
                    await bot.send_message(message.channel, "Battle Ready!\n" + uscount + " US: " + separator.join([user.mention for user in queueus]) + "\n" + gecount + " GE: " + separator.join([user.mention for user in queuege]) + "\nPlease join the 'Decide the City' voice room to get your battle going! Once all 5 members from each faction join you are ready to pop a war battle!")
                    await bot.send_message(message.channel, embed=us)
                    await bot.send_message(message.channel, embed=ge)
                if len(queueus) <= len(queuesu):
                    await bot.send_message(message.channel, "Battle Ready!\n" + uscount + " US: " + separator.join([user.mention for user in queueus]) + "\n" + sucount + " SU: " + separator.join([user.mention for user in queuesu]) + "\nPlease join the 'Decide the City' voice room to get your battle going! Once all 5 members from each faction join you are ready to pop a war battle!")
                    await bot.send_message(message.channel, embed=us)
                    await bot.send_message(message.channel, embed=su)

    if message.content.lower().startswith('!remove us'):
        """message"""
        userID = message.author.id
        user = message.author
        await bot.send_message(message.channel, "<@%s> Removed from queue!" % (userID))
        """action"""
        queueus.remove(user)

    """SU QUEUE"""

    if message.content.lower().startswith('!q su'):
        """message"""
        userID = message.author.id
        user = message.author
        """action"""
        if user in queuege:
            print("Yes, 'at' found in List : " , queuege)
            await bot.send_message(message.channel, "<@%s> You are already in the German queue!" % (userID))
        elif user in queueus:
            print("Yes, 'at' found in List : " , queueus)
            await bot.send_message(message.channel, "<@%s> You are already in the US queue!" % (userID))
        elif user in queuesu:
            print("Yes, 'at' found in List : " , queuesu)
            await bot.send_message(message.channel, "<@%s> You are already in the SU queue!" % (userID))
        else:
            await bot.send_message(message.channel, "<@%s> You are now queued for the Soviet Union!" % (userID))
            queuesu.append(user)
            print(queuesu)

            if queuesuComplete(queuesu):
                separator = ", "
                await bot.send_message(message.channel, "Full SU queue!")
                """Check GE and SU Queue"""
                if len(queuesu) <= len(queuege):
                    await bot.send_message(message.channel, "Battle Ready!\n" + sucount + " SU: " + separator.join([user.mention for user in queuesu]) + "\n" + gecount + " GE: " + separator.join([user.mention for user in queuege]) + "\nPlease join the 'Decide the City' voice room to get your battle going! Once all 5 members from each faction join you are ready to pop a war battle!")
                    await bot.send_message(message.channel, embed=su)
                    await bot.send_message(message.channel, embed=ge)
                if len(queuesu) <= len(queueus):
                    await bot.send_message(message.channel, "Battle Ready!\n" + sucount + " SU: " + separator.join([user.mention for user in queuesu]) + "\n" + uscount + " US: " + separator.join([user.mention for user in queueus]) + "\nPlease join the 'Decide the City' voice room to get your battle going! Once all 5 members from each faction join you are ready to pop a war battle!")
                    await bot.send_message(message.channel, embed=su)
                    await bot.send_message(message.channel, embed=us)

    if message.content.lower().startswith('!remove su'):
        """message"""
        userID = message.author.id
        user = message.author
        await bot.send_message(message.channel, "<@%s> Removed from queue!" % (userID))
        """action"""
        queuesu.remove(user)

    """STATUS"""
    
    if message.content.lower().startswith('!status'):
        separator = ", "
        #await bot.send_message(message.channel, gecount + " Queued for Germany | " + separator.join([user.mention for user in queuege]) + "\n" + uscount + " Queued for United States | " + separator.join([user.mention for user in queueus]) + "\n" + sucount + " Queued for Soviet Union | " + separator.join([user.mention for user in queuesu]))
        #await bot.send_message(message.channel, uscount + " Queued for United States: " + separator.join([str(user) for user in queueus]))
        #await bot.send_message(message.channel, sucount + " Queued for Soviet Union: " + separator.join([str(user) for user in queuesu]))
        """
        if EnquiryGE(queuege):
            separator = ", "
            await bot.send_message(message.channel, gecount + " Queued for Germany: " + separator.join([str(user) for user in queuege]))
            #await bot.send_message(message.channel, gecount + " Queued for Germany: " + separator.join([user.mention for user in queuege])) 
        else: 
            await bot.send_message(message.channel, "No one queued for Germany")
        if EnquiryUS(queueus):
            separator = ", "
            await bot.send_message(message.channel, uscount + " Queued for United States: " + separator.join([str(user) for user in queueus]))
        else: 
            await bot.send_message(message.channel, "No one queued for United States")
        if EnquirySU(queuesu):
            separator = ", "
            await bot.send_message(message.channel, sucount + " Queued for Soviet Union: " + separator.join([str(user) for user in queuesu]))
        else: 
            await bot.send_message(message.channel, "No one queued for Soviet Union")
        """
        
        """STATUS EMBED"""
        user = message.author
        #if message.content.lower().startswith('!status'):
        embedstatus = discord.Embed(title="Status", colour=0x0000FF)
        if len(queuege) == 0:
            embedstatus.add_field(name=str(gecount) + " Queued for Germany", value="No one", inline=True)
        else:
            embedstatus.add_field(name=str(gecount) + " Queued for Germany", value=(separator.join([user.mention for user in queuege])), inline=True)

        if len(queueus) == 0:
            embedstatus.add_field(name=str(uscount) + " Queued for United States", value="No one", inline=False)
        else:
            embedstatus.add_field(name=str(uscount) + " Queued for United States", value=(separator.join([user.mention for user in queueus])), inline=False)
        
        if len(queuesu) == 0:
            embedstatus.add_field(name=str(sucount) + " Queued for Soviet Union", value="No one", inline=False)
        else:
            embedstatus.add_field(name=str(sucount) + " Queued for Soviet Union", value=(separator.join([user.mention for user in queuesu])), inline=False)
        
        await bot.send_message(message.channel, embed=embedstatus)

    """CLEARING"""

    if message.content.lower().startswith('!clear ge'):
        if "admin" in [y.name.lower() for y in message.author.roles]:
            queuege.clear()
            if EnquiryGE(queuege):
                separator = ", "
                await bot.send_message(message.channel, "Queued for Germany: " + separator.join([user.mention for user in queuege]))
            else: 
                print("Empty List")
                await bot.send_message(message.channel, "No one queued for Germany")
        else:
            await bot.send_message(message.channel, "Admin Only")
                    
    if message.content.lower().startswith('!clear us'):
        if "admin" in [y.name.lower() for y in message.author.roles]:
            queueus.clear()
            if EnquiryUS(queueus):
                separator = ", "
                await bot.send_message(message.channel, "Queued for United States: " + separator.join([user.mention for user in queueus]))
            else: 
                print("Empty List")
                await bot.send_message(message.channel, "No one queued for United States")
        else:
            await bot.send_message(message.channel, "Admin Only")

    if message.content.lower().startswith('!clear su'):
        if "admin" in [y.name.lower() for y in message.author.roles]:
            queuesu.clear()
            if EnquirySU(queuesu):
                separator = ", "
                await bot.send_message(message.channel, "Queued for Soviet Union: " + separator.join([user.mention for user in queuesu]))
            else: 
                print("Empty List")
                await bot.send_message(message.channel, "No one queued for Soviet Union")
        else:
            await bot.send_message(message.channel, "Admin Only")

    if message.content.lower().startswith('!clear all'):
        if "admin" in [y.name.lower() for y in message.author.roles]:
            queuege.clear()
            queueus.clear()
            queuesu.clear()
            if EnquiryGE(queuege):
                separator = ", "
                await bot.send_message(message.channel, "Queued for Germany: " + separator.join([user.mention for user in queuege]))
            elif EnquiryUS(queueus):
                separator = ", "
                await bot.send_message(message.channel, "Queued for United States: " + separator.join([user.mention for user in queueus]))
            elif EnquirySU(queuesu):
                separator = ", "
                await bot.send_message(message.channel, "Queued for Soviet Union: " + separator.join([user.mention for user in queuesu]))
            else: 
                print("Empty List")
                await bot.send_message(message.channel, "No one queued for Germany\nNo one queued for United States\nNo one queued for Soviet Union")
        else:
            await bot.send_message(message.channel, "Admin Only")

#Goes at bottom
"""DO NOT TOUCH"""
bot.run("NTc1OTYyMzczMjQwNjUxNzc3.XNPrZQ.mYm51RKRdUT-OYRKK3uiuQqEMYY")
