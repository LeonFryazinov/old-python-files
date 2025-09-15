import discord
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())

messages_str = ""

@bot.command()
async def scrape(ctx, channel):
    global messages_str
    channel = bot.get_channel(int(channel))
    i = 1
    print("started count")
    async for msg in channel.history(limit=1_000_000):  # Adjust the limit as needed
        messages_str += msg.content
        print(i)
        
        i += 1
    
    with open("messages.txt", "w",encoding="utf-8") as file:
        file.write(messages_str)
    print("finished scrape")


bot.run('bot token')