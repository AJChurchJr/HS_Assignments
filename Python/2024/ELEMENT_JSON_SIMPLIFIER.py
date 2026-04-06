import json

files = ("Loffin","TulipNanth","AtherMuffin")

for i in range(3):
    
    with open("./"+str(files[i]) +".json","r",encoding="utf-8") as raw:
        file = json.load(raw)

    #only taking the messages
    file = file['messages']

    #only taking the content of the messages
    for j in range(len(file)):
        file[j] = file[j]['content']
        


    #only taking the body if it's there and if it's not an error
    output = []
    for j in range(len(file)):
        if "body" not in file[j].keys():
            continue
        elif "msgtype" in file[j].keys() and file[j]["msgtype"] == "m.bad.encrypted":
            output.append("-----NOTFOUND-----")
        else:
            output.append(file[j]['body'])

    #saving as json
    with open("./"+str(files[i]) +"2.json","w",encoding="utf-8") as raw:
        json.dump(output,raw,indent=4)


    #creating a text document as well
    output_str = ""
    for line in output:
        output_str += "\n\n"
        output_str += str(line)

    #saving as json
    with open("./"+str(files[i]) +"3.txt","w",encoding="utf-8") as raw:
        raw.write(output_str)
