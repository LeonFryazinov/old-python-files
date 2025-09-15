import random
import json
import discord
import os
from discord.ext import commands
import translators as ts
import spotipy

lang = ["en","zh","ar","ru","fr","de","es","pt","it","ja","ko","el","nl","hi","tr","ms","th","vi","id","pl","mn","cs","hu","et","bg","da","fi","ro","sv","sl","bs","fa","sr","tl","ht","ca","hr","lv","lt","ur","uk","cy","sw","sm","sk","af","no","bn","mg","mt","gu","ta","te","pa","am","az","be","ceb","eo","eu","ga"]



with open(r"word_weights.json", 'r',encoding="utf-8") as f:
    # Load the JSON data from the file into a Python dictionary
    word_weights = json.load(f)
with open(r"words.json", 'r',encoding="utf-8") as f:
    # Load the JSON data from the file into a Python dictionary
    words = json.load(f)

def generate_message(starting_word=None):
    #pick a random starting word
    print("command triggered")
    words_list = list(words.keys())
    weights = list(words.values())
    if starting_word == None:
        starting_word = random.choices(words_list,weights)[0]
    elif not starting_word in words_list:
        starting_word = random.choices(words_list,weights)[0]
    end_chance = 1

    
    #not random.randint(0,35) in range(end_chance)
    sentence = [starting_word]
    while not random.randint(0,35) in range(end_chance): # 
        if not sentence[end_chance-1] in word_weights:
            message = " ".join(sentence)
            with open(r"messages_sent.txt", "a",encoding="utf-8") as t:
                t.write(message)
            return message
        
        next_word_list = list(word_weights[sentence[end_chance-1]].keys())
        next_word_weights = list(word_weights[sentence[end_chance-1]].values())
        if next_word_list == []:
            message = " ".join(sentence)
            with open(r"messages_sent.txt", "a",encoding="utf-8") as t:
                t.write(message)
            return message
        next_word = random.choices(next_word_list,next_word_weights)[0]
        sentence.append(next_word)
        
        end_chance += 1
    print(end_chance)
    
    message = " ".join(sentence)

    return message


def translate_mes(message: str):
    
    translated_message = message
    for i in range(10):
        new_lang = random.choice(lang)
        translated_message = ts.translate_text(translated_message,"google",to_language=new_lang)
        print(new_lang)
    
    
    translated_message = ts.translate_text(translated_message,"google",to_language="en")
    return translated_message



if True:
    BOT_TOKEN = "bot token"
bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())
@bot.event
async def on_message(message):
    
    if message.author.id != "author id":
        print("not bot")
        if message.content == "?motivate":
            
            await message.channel.send(generate_message())

        elif "?translate_message" in message.content:
            mess = message.content[18:]
            await message.channel.send(translate_mes(mess))

        elif "?prompt" in message.content:
            prompt = message.content[8:]
            await message.channel.send(generate_message(prompt))
        elif message.content == "?help":
            await message.channel.send("```The commands\n?motivate - generates a random sentence\n?prompt (word) - generates a random sentence begining with the word provided,\n  unless the word is not in the data base.```")
        elif "?add_to_queue" in message.content:
            prompt = message.content[14:]
        else:
            print("message sent, chance of generation")
            rand_chance = random.randint(0,4)
            print(rand_chance)
            if rand_chance == 1:
                #generate message
                print("message sent")
                await message.channel.send(generate_message())



    


bot.run(BOT_TOKEN)
