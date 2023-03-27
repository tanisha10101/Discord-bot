import discord
import os

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hi')

    if message.content.startswith('ping'):
        await message.channel.send('pong')

client.run(
    'MTA4OTc5NTkzNjA4NTA5MDM2NA.G_xjrr.tIH4yafvbEvv3kC1n3xzPyLYkkSyBFRszr-I8Y')
