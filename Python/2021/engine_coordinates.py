import msvcrt
def cls():
    import os

    os.system('cls' if os.name=='nt' else 'clear')
    return
xpos=0
ypos=0

def movement(xpos,ypos):
    #updown section
    register = ord(msvcrt.getch())
    if register==224:
        return ('no', 'no')
    if register==72 or register==80:
        if register==72:
            ypos+=1
        elif register==80:
            ypos-=1
        return(ypos, 'y')
    #leftright section
    elif register==75 or register==77:
        if register==75:
            xpos-=1
        elif register==77:
            xpos+=1
        return(xpos,'x')


def dungeonengine(xpos,ypos):
    while True:
        movement_return=movement(xpos,ypos)
        cls()
        if movement_return[0]=='no':
            continue
        else:
            if movement_return[1]=='y':
                ypos=movement_return[0]
            elif movement_return[1]=='x':
                xpos=movement_return[0]

        print(str(xpos)+','+str(ypos))

dungeonengine(xpos,ypos)
