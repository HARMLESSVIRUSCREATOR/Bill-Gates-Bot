import discord


from typing import Text
import discord
from discord import client
import os

client = discord.Client()

@client.event
async def on_ready():
          print('{0.user} is online! '.format(client))

@client.event
async def on_message(message):
        if message.author == client.user:
                return
        if message.content.startswith('/./tell I am dumb'):
                await message.channel.send('you are a dumb looser hehe :)')
        if message.content.startswith('//you are noob'):
                await message.channel.send('all your money has been scammed :)')
        if message.content.startswith("dir..change_type = leading_edge"):
                await message.channel.send("changing type to leading edge.....")
                await message.channel.send("traceback_call_error, leading_edge is a unstable technology and thus should not be added into stable systems!")
        if message.content.startswith("dir..update_system:system.update:config.:update:system_full_upgrade"):
                await message.channel.send("updating system via pkgupdater.....")
                await message.channel.send("system is now looking for latest package databases for updates (if any)")
                await message.channel.send("2 packages are being upraded")
                await message.channel.send("the files systemdirrunner32.pkg and system3290.l.pkg have been replaced with their newer versions")
                await message.channel.send("task completed, exiting pkgupdater")
        if message.content.startswith("dir..funny meme pls"):
                await message.channel.send("the faq.")
                await message.channel.send("https://www.youtube.com/watch?v=HfeervqhY9Y")
        if message.content.startswith("dir..minicraft meme pls"):
                await message.channel.send("when you realise that you are so rich and you play pirated minicraft")
        if message.content.startswith("dir..joke on dank"):
                await message.channel.send("that freaking patreon noob dank memer, ")
        if message.content.startswith("dir..never gonna g you up"):
                await message.channel.send("always gonna let you down")
client.run("here you will type your bot token, without this the bot cannot take advantage of this script.")
