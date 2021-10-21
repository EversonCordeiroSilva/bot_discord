import datetime

from discord.ext import commands
from discord.ext.commands import has_permissions
from pytz import timezone
import discord
import asyncio
import os
from dotenv import load_dotenv
import pyexcel_ods

load_dotenv()
TOKEN = os.getenv('TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
client  = discord.Client()
semana = {0: 'segunda', 1: 'terca', 2: 'quarta', 3: 'quinta', 4: 'sexta', 5: 'sabado', 6: 'domingo'}
allowed_mentions = discord.AllowedMentions(everyone=True)


def excel(diaDaSemana='domingo'):
    data = pyexcel_ods.get_data("emissarioList/" + diaDaSemana + ".ods")
    # print()
    excel = None
    for d in data.items():
        for f in d:
            excel = f
    # print(excel)
    del excel[0:2]
    del excel[-1]
    del excel[-1]
    return excel


async def my_background_task():
    await client.wait_until_ready()
    # channel = client.get_channel(id=894572084670373908) # replace with channel_id
    fuso_horario = timezone('America/Sao_Paulo')

    while not client.is_closed():
        # importar
        for e in excel(semana[datetime.datetime.today().weekday()]):
            horaDoBoss = str(format(e[2], '%H:%M'))
            # now = datetime.datetime.now() + datetime.timedelta(minutes=19) #para testes
            now = datetime.datetime.now().astimezone(fuso_horario).time()
            now = str(format(now, '%H:%M'))
            print('Horario atual: '+now)
            print('Horario do boss: '+horaDoBoss)
            if (horaDoBoss == now):
                mensagem = "Atenção!\n@everyone\n" + e[0] + "de Lv. " + str(e[1]) + " Apareceu! \nLocalização: " + e[3] + "\nRecompensa: " + e[4] + "\nFama points: " + str(e[5]) + "\nObservações adicionais: " + e[6]
                for guild in client.guilds:
                    for channel in guild.channels:
                        try:
                            if channel.type == discord.ChannelType.text:
                                if channel.permissions_for(guild.me).send_messages:
                                    await client.get_channel(channel.id).send(content=mensagem, allowed_mentions=allowed_mentions)
                        except:
                            print('Nao foi possivel enviar uma mensagem...')
        await asyncio.sleep(60)  # task runs every 60 seconds


def montarMensagem(diaDaSemana):
    mensagem = ""
    for e in excel(diaDaSemana):
        mensagem += "\n-----\nHorário: " + str(e[2]) + "\n" + e[0] + "de Lv. " + str(e[1]) + "\nLocalização: " + e[3] + "\nRecompensa: " + e[4] + "\nFama points: " + str(e[5]) + "\nObservações adicionais: " + e[6] + "\n-----"
    return mensagem


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    prefix = '!'
    if message.content.startswith(prefix):
        diaDaSemana = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
        carregando = 'Carregando lista de emissários...'
        sucesso = 'Carregado! Aqui está: '

        if message.content.startswith(prefix + diaDaSemana[0]):
            await message.channel.send(carregando)
            m = montarMensagem(diaDaSemana[0])
            await message.channel.send(sucesso)
            await message.channel.send(m)

        if message.content.startswith(prefix + diaDaSemana[1]):
            await message.channel.send(carregando)
            m = montarMensagem(diaDaSemana[0])
            await message.channel.send(sucesso)
            await message.channel.send(m)

        if message.content.startswith(prefix + diaDaSemana[2]):
            await message.channel.send(carregando)
            m = montarMensagem(diaDaSemana[2])
            await message.channel.send(sucesso)
            await message.channel.send(m)

        if message.content.startswith(prefix + diaDaSemana[3]):
            await message.channel.send(carregando)
            m = montarMensagem(diaDaSemana[3])
            await message.channel.send(sucesso)
            await message.channel.send(m)

        if message.content.startswith(prefix + diaDaSemana[4]):
            await message.channel.send(carregando)
            m = montarMensagem(diaDaSemana[4])
            await message.channel.send(sucesso)
            await message.channel.send(m)

        if message.content.startswith(prefix + diaDaSemana[5]):
            await message.channel.send(carregando)
            m = montarMensagem(diaDaSemana[5])
            await message.channel.send(sucesso)
            await message.channel.send(m)

        if message.content.startswith(prefix + diaDaSemana[6]):
            await message.channel.send(carregando)
            m = montarMensagem(diaDaSemana[6])
            await message.channel.send(sucesso)
            await message.channel.send(m)
    # await client.process_commands(message)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

if __name__ == "__main__":
    client.loop.create_task(my_background_task())
    client.run(TOKEN)
