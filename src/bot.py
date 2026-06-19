import discord
import asyncio
import os
from dotenv import load_dotenv
from checker import get_test_results

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

last_known_project = None

async def checking_moulinette():
    global last_known_project

    await client.wait_until_ready()
    channel = await client.fetch_channel(CHANNEL)

    while True:
        print("🔍 Checking the moulinette")
        data = get_test_results()
        
        if data:
            results = data["results"]
            last = results[-1]
            title = last["context"]["title"]
            date = last["properties"]["date"]
        
        if last != last_known_project:
            last_known_project = last
            await channel.send(
                f"🚀 **New Moulinette's result !**\n"
                f"📁 Project : **{title}**\n"
                f"📅 Date : {date}\n"
                f"✅ Prerequisites Mark : {last['prerequisitesMark']}"
            )
            print(f"Notification sent for : {title}")
        else:
            print(f"No changes - last project : {title}")
        
        await asyncio.sleep(10)

@client.event

async def on_ready():
    print(f" ✅ Bot connected as : {client.user}")
    await asyncio.ensure_future(checking_moulinette())
client.run(TOKEN)