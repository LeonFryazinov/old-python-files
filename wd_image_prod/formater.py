
messages_str = ""

with open(r"Messages.txt","r",encoding="utf-8") as file:
    messages_str = file.read()

    

formated_str = messages_str.replace(" ","")
formated_str = formated_str.replace("\n","")

with open(r"Messages_formated.txt","w",encoding="utf-8") as file:
    file.write(formated_str)


