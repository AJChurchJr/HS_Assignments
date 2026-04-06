#thanks to minzkraut.com for base code
from PIL import Image
import os,math,time

#making values
def generate_sprite(path:str,
    columns:int = 5,
    output_name:str="output",
    column_cap = True #if false, special occurs
                    ):
    
    #definitions
    files = []
    frames = []

    tile_width = 0
    tile_height = 0

    spritesheet_width = 0
    spritesheet_height = 0


    #error checking: adding end slashes
    if path[len(path)-1]!= "\\" and path[len(path)-1]!="/":
        path += "\\"

    try:
        files = os.listdir(path)
    except:
        print("FOLDER NOT PRESENT.")
        return


    #iterating through every file to add to the files list
    invalid_files = []
    for _ in files: 
        try:
            with Image.open(path+_) as img:
                frames.append(img.getdata())
        except:
            invalid_files.append(_)
    print(str(len(invalid_files)),"INVALID FILES:",str(invalid_files) )
    del invalid_files


    #error checking: no images in folder
    if len(frames)==0:
        print("NO IMAGES IN FOLDER.")
        return


    #tile size
    tile_width,tile_height = frames[0].size[0],frames[0].size[1]


    #spritesheet dimensions / columns
    if len(frames) > columns :
        rows = math.ceil(len(frames)/columns)
        spritesheet_width = tile_width * columns
        spritesheet_height = tile_height * rows
    else:
        rows = 1
        spritesheet_width = tile_width*len(frames)
        spritesheet_height = tile_height


    #making file
    spritesheet = Image.new("RGBA",(int(spritesheet_width),int(spritesheet_height)))
    spritesheet.save(path + output_name + ".png" ,"PNG")


    #aligning images
    for current_frame in frames:
        top = tile_height * math.floor((frames.index(current_frame))/columns)
        left = tile_width * (frames.index(current_frame) % columns)
        bottom = top + tile_height
        right = left + tile_width

        box = (
            left,
            top,
            right,
            bottom)
        box = [int(i) for i in box]

        cut_frame = current_frame.crop((0,0,tile_width,tile_height))
        spritesheet.paste(cut_frame,box)
    
    spritesheet.save(path + output_name + ".png","PNG")

    

    #giving output file

    with open(path + output_name + ".txt", "w") as file:
        file.write(
            str(
                {  
                    "IMAGE":"NONE",
                    "ANIM":"NONE",
                    "SHEET_SIZE":(spritesheet_width,spritesheet_height),
                    "TILE_SIZE":(tile_width,tile_height),
                    "ROWS/COLUMNS":(rows,columns if column_cap else len(frames)),
                    "colorkey":[1,2,3],
                    "anim":{}
                }
            )
        )


    del box,spritesheet,cut_frame,frames,files,_,top,left,bottom,right

#GENERATING FOR EVERYTHING IN CHARACTERS
##for folder in os.listdir("./images/raw_characters"):
##    
##    generate_sprite(
##        path = "./images/raw_characters/"+folder+"/",
##        columns = 999,
##        output_name = "../../characters/"+folder,
##        column_cap = False)

while True:
    generate_sprite(path=input("Enter image path:"),columns=999,output_name = "Enter file name:",column_cap=False)


