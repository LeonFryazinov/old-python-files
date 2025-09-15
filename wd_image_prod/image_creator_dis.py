import discord
from discord.ext import commands
from PIL import Image
import colorsys
from math import *

bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())



@bot.command()
async def create_image(ctx, channel):
    messages_str = ""
    
    channel = bot.get_channel(int(channel))
    file_name = channel.name + "_image.png"
    i = 1
    print("started count")
    async for msg in channel.history(limit=1_000_000):  # Adjust the limit as needed
        messages_str += msg.content
        print(i)
        
        i += 1
    
    
    print("finished scrape")
    formated_str = format(messages_str)
    create_picture(formated_str,file_name)








def format(messages_str):
    print("formating")
    formated_str = messages_str.replace(" ","")
    formated_str = formated_str.replace("\n","")
    formated_str = formated_str.replace(" ","")
    return formated_str



def create_picture(messages_str,filename):
    print("image started creation")
    width = int(ceil(sqrt(float(len(messages_str)))))
    height = int(ceil(float(len(messages_str))/width))



    img = Image.new('RGB', (width,height))

    i = 0

    for y in range(height):
        for x in range(width):
            
            try:

                h = max(min(ord(messages_str[i]),140),32)-32
            except:
                continue
            hue = h/ 108.0
            r,g,b = colorsys.hsv_to_rgb(hue,1.0,1.0)

            r,g,b, = int(r*255), int(g*255), int(b*255)

            
            img.putpixel((x,y), (r, g, b))

            i += 1

    
    img.save(filename)
    print("created image")


bot.run('bot token')