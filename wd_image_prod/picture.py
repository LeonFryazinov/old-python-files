from PIL import Image
import colorsys
ascii_values = {}
messages_str = ""

with open(r"Messages_formated.txt","r",encoding="utf-8") as file:
    messages_str = file.read()
    for i in messages_str:
        if ord(i) in ascii_values.keys():
            ascii_values[ord(i)]+= 1
        else:
            ascii_values[ord(i)] = 1

sorted_dict = dict(sorted(ascii_values.items(), key=lambda item: item[0]))

width = 1156
height = 1155

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


img.save(r"image4.png")

#image size 1156x1155
