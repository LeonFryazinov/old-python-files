from PIL import Image, ImageDraw
import time
keys = {
    "c1" : "c#1",
    "c#1" : "d1",
    "d1" : "d#1",
    "d#1" : "e1",
    "e1" : "f1",
    "f1" : "f#1",
    "f#1" : "g1",
    "g1": "g#1",
    "g#1" : "a1",
    "a1" : "a#1",
    "a#1" : "b1",
    "b1" : "c2",
    "c2" : "c#2",
    "c#2" : "d2",
    "d2" : "d#2",
    "d#2" : "e2",
    "e2" : "f2",
    "f2" : "f#2",
    "f#2" : "g2",
    "g2" : "g#2",
    "g#2" : "a2",
    "a2" : "a#2",
    "a#2" : "b2",
    "b2" : "c3",
    "c3": "c#3",#
    "c#3" : "d3",
    "d3" : "d#3",
    "d#3" : "e3",
    "e3" : "f3",
    "f3" : "f#3",
    "f#3": "g3",#
    "g3" : "g#3",
    "g#3" : "a3",
    "a3" : "a#3",
    "a#3" : "b3",
    "b3" : "c4",
    "c4": "c#4",
    "c#4" : "d4",
    "d4" : "d#4",
    "d#4" : "e4",
    "e4" : "f4",
    "f4" : "f#4",
    "f#4": "g4",
    "g4" : "g#4",
    "g#4" : "a4",
    "a4" : "a#4",
    "a#4" : "b4",
    "b4" : "c5",
    "c5" : "c5"
}

keys_pos = {
    "c1" : (220,1450),
    "c#1" : (290,1300),
    "d1" : (350,1450),#130 each
    "d#1" : (410,1300), # 120
    "e1" : (480,1450),
    "f1" : (610,1450),
    "f#1" : (675,1300),
    "g1" : (740,1450),
    "g#1" : (770,1300),
    "a1" : (870,1450),
    "a#1" : (890,1300),
    "b1" : (1000,1450),
    "c2" : (1130,1450),
    "c#2" : (1575,1300),
    "d2" : (1260,1450),
    "d#2" : (1695,1300),
    "e2" : (1390,1450),
    "f2" : (1520,1450),
    "f#2" : (1575,1300),
    "g2" : (1650,1450),
    "g#2" : (1695,1300),
    "a2" : (1780,1450),
    "a#2" : (1815,1300),
    "b2" : (1910,1450),
    "c3": (2010,1450),
    "c#3" : (2085,1300),
    "d3" : (2140,1450),
    "d#3" : (2195,1300),
    "e3" : (2270,1450),
    "f3" : (2400,1450),
    "f#3" : (2460,1300),#
    "g3" : (2530,1450),
    "g#3" : (2585,1300),#
    "a3" : (2660,1450),
    "a#3" : (2700,1300),#
    "b3" : (2790,1450),
    "c4": (2920,1450)

}





e_string = None
B_string = None
G_string = None
D_string = None
A_string = None
E_string = None

E_key = None
A_key = None
D_key = None
G_key = None
B_key = None
e_key = None


def find_key(num,start_key):
    if start_key == "c5":
        print("OVERFLOW")
        print("OVERFLOW")
        print("OVERFLOW")
        print("OVERFLOW")
        print("OVERFLOW")
        print("OVERFLOW")
        print("OVERFLOW")

    if num == "":
        return None
    if int(num) == 0:
        return start_key


    new_key = keys[start_key]
    return find_key(int(num)-1,new_key)

def get_input():
    global E_key, A_key, D_key, G_key, B_key, e_key 
    e_string = input("what number on e: ")
    B_string = input("what number on B: ")
    G_string = input("what number on G: ")
    D_string = input("what number on D: ")
    A_string = input("what number on A: ")
    E_string = input("what number on E: ")


    E_key = find_key(E_string,"e1")
    A_key = find_key(A_string,"a1")
    D_key = find_key(D_string,"d2")
    G_key = find_key(G_string,"g2")
    B_key = find_key(B_string,"b2")
    e_key = find_key(e_string,"e3")


def show_piano():
    piano = Image.open(r"piano.png")
    draw = ImageDraw.Draw(piano)

    if E_key != None:
        pos = keys_pos[E_key]
        draw.circle(pos,20,(255,0,0))
    if A_key != None:
        pos = keys_pos[A_key]
        draw.circle(pos,20,(255,0,0))
    if D_key != None:
        pos = keys_pos[D_key]
        draw.circle(pos,20,(255,0,0))
    if G_key != None:
        pos = keys_pos[G_key]
        draw.circle(pos,20,(255,0,0))
    if B_key != None:
        pos = keys_pos[B_key]
        draw.circle(pos,20,(255,0,0))
    if e_key != None:
        pos = keys_pos[e_key]
        draw.circle(pos,20,(255,0,0))





    piano.show()

    piano.save(r"C:\Users\russi\OneDrive\Documents\python scripts\Tab to piano\output\ " + str(time.time())+".png")

def print_notes():
    global E_key, A_key, D_key, G_key, B_key, e_key 
    if E_key != None:
        print(E_key + ", ", end="")
    if A_key != None:
        print(A_key + ", ", end="")
    if D_key != None:
        print(D_key + ", ", end="")
    if G_key != None:
        print(G_key + ", ", end="")
    if B_key != None:
        print(B_key + ", ", end="")
    if e_key != None:
        print(e_key)
    print("\n")



while True:
    get_input()
    print_notes()


