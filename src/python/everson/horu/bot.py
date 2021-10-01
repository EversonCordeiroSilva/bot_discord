import discord
from discord.ext import commands as commands

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)
#clientVoice = discord.VoiceClient()

@client.event
async def on_ready():
    print("Wait... I awaken... shut up!")
    print("----------------------------")

@client.event
async def on_message(message):
    autor = str(message.author)
    eu = "Everson Silva#6488"
    horu = "Horu#3427"
    if(autor == eu):
        if message.author == client.user:
            return

        if message.content.startswith('Helloworld!'):
            await message.channel.send('I am Horu a cleric in Grand Fantasia! Play with me.')

        if message.content.startswith('I want to see you Horu!'):
            await message.channel.send("I'm coming to you...")
            await join(message)

    elif(autor == horu):
        return

    else:
        await message.channel.send("Shut up! Bastard!")

    await client.process_commands(message)

@client.command()
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        print(channel)
        await channel.connect()
    else:
        await ctx.send("I not found you... Buá!!!!")
    await client.process_commands(ctx)

@client.command()
async def bye(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I see you again later my man...")
    else:
        await ctx.send("You not see me...")

client.run('ODkyODM1MDM2ODg0MjU4ODM3.YVSrbA.wgBTWnaOOZnZID3ae94AQMD-hlM')
