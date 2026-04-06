import pygame
import math
from time import sleep as wait
print('physics program by Andrew Church\nDown is positive y velocity\nRight is positive x velocity')


window = pygame.display.set_mode((640,480))
clock=pygame.time.Clock()
run=True

#info vert and horiz
x = {'vi':0,'v':0,'a':0,'d':0}
y = {'vi':0,'v':0,'a':9.8,'d':0}
y['vi'] = y['v'] = -50
x['vi'] = x['v'] = 30
#placeholder
point=pygame.Surface((25,25))
pygame.draw.rect(point,"#FFFFFF",pygame.Rect(25,25,0,0)) #time
time = 0 #what the distance bases change by velocity and acceleration
        
time_step = 1/5 #float(input("time acceleration per iteration?"))

while run:
    #updating global times
    time += time_step
    #working on y right now
    y['v'] = round(((y['a']*time) + y['vi']),4)
    y['d'] = round((y['vi']*time) + (0.5*y['a']*(time**2)),4)
    x['v'] = round(((x['a']*time) + x['vi']),4)
    x['d'] = round((x['vi']*time) + (0.5*x['a']*(time**2)),4)

    #draw
    window.fill("#008800")
    window.blit(point,(x['d'],480+y['d']))
    pygame.display.update()
    clock.tick(30)

    #event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run=False


pygame.QUIT()
exit()
    
    
