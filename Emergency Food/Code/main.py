import discord
import time

import sys
import prompts
import refresh

from discord import app_commands

# Base Calls
prompt = prompts.Prompt()
remind = refresh.Refresh()
check = remind.CheckAll()

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False
        
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"We have logged in as {self.user}.")
        
        # CALL DAILY FUNCTION
        await daily()

client = aclient()
tree = app_commands.CommandTree(client)

# All Commands
@tree.command(name = "spiral", description = "Paimon will tell you how many days are left until Spiral Abyss resets!")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello! " + prompt.spiral())

# Events
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "emergency food" in message.content.lower():
        await message.channel.send(
            prompt.annoy().format(message.author.mention))

    if client.user in message.mentions:
        await message.channel.send(
            prompt.pinged().format(message.author.mention))

# Function for daily reminder.
@client.event
async def daily():
    
    # CHANNEL FOR REMINDERS
    # Copy and paste the channel ID in the next line for the dedicated reminders.
    channel_id = 1001671131482312705
    channel = client.get_channel(channel_id)

    # Code to send messages.
    await channel.send(prompt.startup())

    if remind:
        await channel.send(prompt.daily())
        if time.localtime(time.time()).tm_wday == 6:
            await channel.send(prompt.beforeWeek())

        if time.localtime(time.time()).tm_wday == 0:
            await channel.send(prompt.weeklyRefresh())
            await channel.send(prompt.weekly())
        
client.run(sys.argv[1])
