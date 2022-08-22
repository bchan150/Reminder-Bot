import discord
import os
import event
import prompts
import refresh
import time

from discord import app_commands

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
        
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id = 818227391670911096))
            self.synced = True
        print(f"We have logged in as {self.user}.")
        

client = aclient()
tree = app_commands.CommandTree(client)

# All Commands
@tree.command(name = "spiral", description = "Paimon will tell you how many days are left until Spiral Abyss resets!", guild = discord.Object(id = 818227391670911096))
async def self(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f"Hello {name}! \n\n" + prompt.spiral())

#Class Initialzation for Events
data = event.Events()

#Class Initialization for Prompts
prompt = prompts.Prompt()
checker = refresh.Refresh()
remind = checker.CheckAll()

@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send(prompt.join())
        break

@client.event
async def on_ready():
    # General Chat Message when bot turns on.
    channel = client.get_channel(1001671131482312705)
    # await channel.send(prompt.startup())

    # Channel for reminders.
    channel = client.get_channel(1001671131482312705)

    # Daily Reminder
    if remind[0]:
        await channel.send(prompt.dailyRefresh())
        await channel.send(prompt.daily())
        if time.localtime(time.time()).tm_wday == 6:
            await channel.send(prompt.beforeWeek())

        # if data.check():
        #     eList = data.eventList()
        #     await channel.send(prompt.events(eList))

        # else:
        #     await channel.send(prompt.noEvents())

    # Weekly Reminder.
    if remind[1]:
        await channel.send(prompt.weeklyRefresh())
        await channel.send(prompt.weekly())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$spiral'):
        await message.channel.send(
            "Hello {}! \n\n".format(message.author.mention) + prompt.spiral())

    if message.content.startswith('$eventAdd'):
        temp = message.content
        if temp == '$eventAdd':
            await message.channel.send("Paimon needs the event you're trying to add in! Format: $eventadd [Name]")
        else:
            temp = temp[10:]
            data.eventAdd(temp)
            await message.channel.send("Paimon just added " + temp + " to the event list!")
            channel = client.get_channel(818958387160023041)
            await channel.send("@here\n\nPaimon has just added " + temp + " to the reminders list! You will now see it in the event list on the next reminder!")

    if message.content.startswith('$eventDelete'):
        temp = message.content
        if temp == '$eventDelete':
            await message.channel.send("Paimon needs the event you're trying to delete! Format: $eventDelete [Index]")
            temp = ""
            for i in data.eventList():
                temp += "> - " + i
            await message.channel.send("Current List:\n" + temp)
        else:
            index = int(temp[13:])
            temp = data.eventList()
            temp = temp[index]
            data.eventDelete(index)
            await message.channel.send("Paimon just deleted " + temp[:-1] + " to the event list!")
            channel = client.get_channel(818958387160023041)
            await channel.send("@here\n\nPaimon has just removed " + temp[:-1] + " from the reminders list!")

    if "emergency food" in message.content.lower():
        await message.channel.send(
            prompt.annoy().format(message.author.mention))

    if client.user in message.mentions:
        await message.channel.send(
            prompt.pinged().format(message.author.mention))

client.run('REDACTED')

# Anything after this is ignored due to how Discord works.
