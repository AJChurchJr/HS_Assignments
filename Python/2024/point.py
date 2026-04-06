import pygame
from math import sin,cos,tan,atan,atan2,degrees

window = pygame.display.set_mode((480,480))
clock = pygame.time.Clock()

FPS = 30
run = True


pointers = []

pointers.append([[240,240],0])

#creating graphical pointer
pointerIMG = pygame.image.load("./test_images/triUP.bmp").convert_alpha()
#pointerIMG = pygame.transform.flip(pointerIMG,False,True)

while run:
    clock.tick(FPS)
    pygame.display.update()
    #handling events
    for event in pygame.event.get():
        #quitting
        if event.type == pygame.QUIT:
            run = False
        #adding new values
        if event.type == pygame.MOUSEBUTTONDOWN:
            pointers.append([list(pygame.mouse.get_pos()),0])
    #modifying pointings
    for pointer in pointers:
        #setting position values
        target = pygame.mouse.get_pos()
        pos = (pointer[0][0] - 15, pointer[0][1] - 15)
        #calculating angle
        pointer[1] = degrees(
            #swapping x and y makes it move in the opposite direction
            #swapping target and pos makes it 
            atan2(
                pos[0]-target[0],
                pos[1]-target[1],
                )
            )
        #rotating image
        img_used = pygame.transform.rotate(pointerIMG,pointer[1])
        #displaying image
        window.blit(img_used,pos)

pygame.QUIT
exit()
        

    
        
