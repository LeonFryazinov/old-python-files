import os
import random
import youtube_dl
from PIL import Image
import speech_recognition as sr
from datetime import datetime
import discord
from gtts import gTTS
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio

BOT_TOKEN = "Bot token"

bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())

admin = 0

voice = None

UPLOAD_FOLDER_PATH = "audio bot"

queue_of_messages = []

bot.remove_command("help")

#sends current time
@bot.command()
async def time(ctx):
    if await can_use(ctx.author.id):
        current_time = datetime.now()
        time_string = current_time.strftime("%H:%M:%S")
        await ctx.send(time_string)

#closes down bot
@bot.command()
async def close(ctx):
    if await can_use(ctx.author.id):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
        await bot.close()
        quit()

#joins voice channel
@bot.command()
async def join(ctx,channel_id:int = None):
    if await can_use(ctx.author.id):
        global voice
        
        if (ctx.author.voice):
            print(channel_id)
            if channel_id == None:
                channel = ctx.message.author.voice.channel
                voice = await channel.connect()    
                
            else:
                channel = bot.get_channel(int(channel_id))
                voice = await int(channel_id).connect    
            
#says something in the voice chat using tts
@bot.command()
async def say(ctx, *args):
    if await can_use(ctx.author.id):
        global message_num
        global voice
        if not ctx.voice_client:
            if ctx.author.voice:
                channel = ctx.message.author.voice.channel
                voice = await channel.connect()
        text = " ".join(args)
        
        file_path = os.path.join(UPLOAD_FOLDER_PATH,"0.mp3")
        tts = gTTS(text)
        tts.save(file_path)
        source = FFmpegPCMAudio(file_path)
        player = voice.play(source)

#hears what is going on in the voice chat
@bot.command()
async def listen(ctx):
    if await can_use(ctx.author.id):
        global voice
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("listening")
                audio = r.listen(source)
                print("recognizing")
                text = r.recognize_sphinx(audio)
                print(text)
                print("finished")
        except Exception as e:
            print(e)

#adds file to my computer
@bot.command()
async def add_file(ctx):
    if await can_use(ctx.author.id):
        if ctx.message.attachments:
            if not os.path.exists(UPLOAD_FOLDER_PATH):
                os.makedirs(UPLOAD_FOLDER_PATH)
            await ctx.send(str(ctx.message.attachments))
        
            attachment = ctx.message.attachments[0]
            allowed_extensions = ['.wav', '.mp3']
            if any(attachment.filename.lower().endswith(ext) for ext in allowed_extensions):
                    
                file_content = await attachment.read()
                
                file_path = os.path.join(UPLOAD_FOLDER_PATH,attachment.filename)
                with open(file_path, 'wb') as file:
                    file.write(file_content)
                
                await ctx.send("file saved")
            else:
                ctx.send("invalid file type")
        else:
            ctx.send("nothing attached")

#plays the audio of youtube videos in voice channel
@bot.command()
async def play_youtube(ctx, link):
    if await can_use(ctx.author.id):
        global voice
        if not ctx.voice_client:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
        ydl_opts = {"format": "bestaudio",
                    "verbose": True}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:    
                info = ydl.extract_info(link, download=False)
                ur12 = info["formats"][0]["url"]
                voice.play(discord.FFmpegPCMAudio(ur12))
            except youtube_dl.utils.RegexNotFoundError:
                print("unable to extract uploader id")
            except Exception as e:
                print(e)
#stops what is currently being played
@bot.command()
async def stop(ctx):
    if await can_use(ctx.author.id):
        global voice
        voice.pause()
#plays an audio file by uploading
@bot.command()
async def play(ctx):
    if await can_use(ctx.author.id):
        global voice
        if (ctx.voice_client):
            if ctx.message.attachments:
                if not os.path.exists(UPLOAD_FOLDER_PATH):
                    os.makedirs(UPLOAD_FOLDER_PATH)
                
                

                attachment = ctx.message.attachments[0]
                allowed_extensions = ['.wav', '.mp3']
                if any(attachment.filename.lower().endswith(ext) for ext in allowed_extensions):
                        
                    file_content = await attachment.read()

                    file_path = os.path.join(UPLOAD_FOLDER_PATH,attachment.filename)
                    with open(file_path, 'wb') as file:
                        file.write(file_content)
                    
                    await ctx.send("file saved")
                    source = FFmpegPCMAudio(file_path)
                    player = voice.play(source)
                    
                else:
                    await ctx.send("invalid file type")
            else:
                await ctx.send("nothing attached")
        else:
            if ctx.author.voice:
                channel = ctx.message.author.voice.channel
                voice = await channel.connect()
                if ctx.message.attachments:
                    if not os.path.exists(UPLOAD_FOLDER_PATH):
                        os.makedirs(UPLOAD_FOLDER_PATH)
                    
                
                    attachment = ctx.message.attachments[0]
                    allowed_extensions = ['.wav', '.mp3']
                    if any(attachment.filename.lower().endswith(ext) for ext in allowed_extensions):
                            
                        file_content = await attachment.read()

                        file_path = os.path.join(UPLOAD_FOLDER_PATH,attachment.filename)
                        with open(file_path, 'wb') as file:
                            file.write(file_content)
                        
                        await ctx.send("file saved")
                        source = FFmpegPCMAudio(file_path)
                        player = voice.play(source)
                        await ctx.send("now playing: " + str(attachment.filename))
                        await ctx.send("audio played")
                    else:
                        await ctx.send("invalid file type")
                else:
                    await ctx.send("nothing attached")
            else:
                await ctx.send("user not in voice channel")
#leaves voice channel
@bot.command()
async def leave(ctx):
    if await can_use(ctx.author.id):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
   

@bot.command()
async def ascii(ctx,enlargement=1):
    if await can_use(ctx.author.id):
        if ctx.message.attachments:
            if len(ctx.message.attachments) == 1:
                attachment = ctx.message.attachments[0]
                allowed_extensions = ['.png', '.jpeg']
                if any(attachment.filename.lower().endswith(ext) for ext in allowed_extensions):
                        
                    file_content = await attachment.read()

                    file_path = os.path.join(UPLOAD_FOLDER_PATH,attachment.filename)
                    with open(file_path, 'wb') as file:
                        file.write(file_content)
                    
                    await ctx.send("file saved")

                    img = Image.open(file_path)
                    w, h = img.size
                    
                    
                    scale = int(enlargement)

                    img.resize((w//scale,h//scale)).save("temp.png")
                    img = Image.open("temp.png")
                    w, h = img.size
                    grid = []
                    for i in range(h):
                        grid.append(["X"] * w)
                    
                    pix = img.load()

                    for y in range(h):
                        for x in range(w):
                            if sum(pix[x,y]) == 0:
                                grid[y][x] = "##"
                            elif sum(pix[x,y]) in range(1,100):
                                grid[y][x] = "XX"
                            elif sum(pix[x,y]) in range(200,300):
                                grid[y][x] = "%%"
                            elif sum(pix[x,y]) in range(300,400):
                                grid[y][x] = "**"
                            elif sum(pix[x,y]) in range(400,500):
                                grid[y][x] = "++"
                            elif sum(pix[x,y]) in range(500,600):
                                grid[y][x] = "//"
                            elif sum(pix[x,y]) in range(600,700):
                                grid[y][x] = "(("
                            elif sum(pix[x,y]) in range(700,750):
                                grid[y][x] = "''"
                            else:
                                grid[y][x] = "  "
                    
                    art = open(r"audio bot\image.txt", "w")

                    for row in grid:
                        art.write("".join(row)+"\n")
                    
                    art.close()
                    print("i have cooked")
                    await ctx.send(file=discord.File("audio bot\image.txt"))
                    

                    
                else:
                    await ctx.send("invalid file type")
            else:
                await ctx.send("too many files attached")
        else:
            await ctx.send("nothing attached")
@bot.command()
async def shelby(ctx):
    if await can_use(ctx.author.id):
        files = os.listdir("audio bot\shelby images")

        files = [f for f in files if os.path.isfile(os.path.join("audio bot\shelby images", f))]

        random_file = random.choice(files)
        shelby_file = os.path.join("audio bot\shelby images", random_file)

        await ctx.send(file=discord.File(shelby_file))
@bot.command()
async def snap(ctx):
    await ctx.send("its coming")

@bot.command()
async def help(ctx):
    await ctx.send("Here are all the commands you can access through poshly bot! \n \n **?time** - sends the current time (looking at the time is a lot more harder than typing a command) \n **?join** - makes poshly bot join whatever voice channel you are currently in. (will not work if not in a voice channel) \n **?say** (message) - will say the message you sent in a voice channel (as long as you are in a voice channel) \n **?play** (music file attached) - Will play a music file through the microphone of the bot (once again as long as you are in a voice channel) \n **?play_youtube** (youtube url) - the same as ?play but with youtube videos (quality is subject to hosts preformance) \n **?stop** - stops all music/speech the bot is saying/playing \n **?leave** - the bot leaves the voice channel \n **?ascii** (scale) - takes in a png or jpg and sends back an ascii art text file, scale spesifies how much you scale down ,so 2 would mean it is half the original size \n **?shelby** - send back a random image of shelby :D \n **?count** - counts up a number by one then sends it back (never gets reset!) \n **?suggestion** - suggest a function the poshly bot should have")

@bot.command()
async def count(ctx):
    if await can_use(ctx.author.id):
        file = open(r"audio bot\count.txt", "r") 
        num = int(file.readline())
        num += 1
        await ctx.send(str(num))
        file.close()
        file = open(r"audio bot\count.txt", "w")
        file.write(str(num))
        file.close()


@bot.command()
async def revoke(ctx, username):
    if ctx.author.id == admin:
        file = open(r"audio bot\revoke_list.txt", "a")
        ident = str(username).strip("<>@")
        file.write(ident+"\n")
        print(ident)
        file.close()

@bot.command()
async def grant(ctx, username):
    if ctx.author.id == admin:
        username = str(username).strip("<>@")
        with open(r"audio bot\revoke_list.txt", "r") as file:
            lines = file.readlines()
        with open(r"audio bot\revoke_list.txt", "w") as file:
            for line in lines:
                if username not in line:
                    file.write(line)




async def can_use(usernId):
    with open(r"audio bot\revoke_list.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip("\n") == str(usernId):
                print(line)
                print(usernId)
                return False
                
    
    return True


@bot.command()
async def suggestion(ctx,*idea):
    idea_string = " ".join(idea)
    print(idea_string)
    with open(r"audio bot\suggestion.txt", "a") as file:
        file.write(idea_string + ": " + str(ctx.author) + "\n")


@bot.command()
async def assign_role(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f"{member.mention} has been assigned the {role.name} role")
@bot.command()
async def jorrep(ctx,):
    await ctx.send("HE SHALL RISE AGAIN!!!")

bot.run(BOT_TOKEN)