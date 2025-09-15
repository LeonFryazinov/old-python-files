from PIL import Image
import colorsys
from math import *
import os
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

    
    filename = filename + "_image.png"
    img.save(filename)
    print("created image")

text_path = input("absolute path of text file: ")
while text_path[-4:] != ".png" and not os.path.exists(text_path):
    print("text file does not exist at that path, please provide a valid path (a .png file)")
    text_path = input("absolute path of text file: ")

filename = os.path.basename(text_path).split('/')[-1]

filename = filename[:-4]
print(filename)
text_str = ""
with open(text_path, "r", encoding="utf-8") as file:
    text_str = file.read()

formated_str = format(text_str)
create_picture(formated_str,filename=filename)
