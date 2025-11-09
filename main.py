from dotenv import load_dotenv 
import os
import asyncio

load_dotenv()
token = str(os.getenv('API_KEY'))
guild = int(os.getenv('CHANNEL_ID'))

import discord

intents = discord.Intents.default()
client = discord.Client(intents=intents)

def make_source():
    return discord.FFmpegPCMAudio(
        'rf.mp3',
        before_options='-stream_loop -1',
        options='-vn'
    )

            

@client.event
async def on_ready():
    channel = client.get_channel(guild) 

    vc = discord.utils.get(client.voice_clients, guild=channel.guild)
    if not vc or not vc.is_connected():
        vc = await channel.connect(reconnect=True)
    
    #vc.source.volume = .5

    while True:
        if not vc.is_playing():
            print(3)
            vc.play(discord.PCMVolumeTransformer(make_source(),volume=.6))
        await asyncio.sleep(1)

client.run(token)
