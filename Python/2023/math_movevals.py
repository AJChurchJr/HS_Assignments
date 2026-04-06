#CODE BY ANDREW CHURCH - PLEASE CREDIT
from math import sqrt

#a point that moves.
class MovingPoint():
    #it takes the point A and point B as an argument, with the optional *speed* value.
    def __init__(self,pointA:tuple,pointB:tuple,speed:int=1):
        #first it saves the two values
        self.pointA,self.pointB = pointA,pointB
        #it then sets the position as where point A originally was, so it can use it separately
        self.position = list(self.pointA)
        #it then calculates the distance and how much the x and y should move every frame
        self.distance = MovingPoint.calc_distance(pointA,pointB)
        self.move_vals = MovingPoint.calc_move_vals(pointA,pointB,self.distance,speed) 

    def update(self):
        #this is what you will run every frame to update MovingPoint's position.
        #note, you could just update the sprite's rect by [MovingPoint object].move_vals(), but as pygame.Rect does not store floats, it will not move accurately as it will round the specified values.
        #what you should do is run update every frame, then set the [bullet]'s position to [MovingPoint Object].position.
        self.position[0] += self.move_vals[0]
        self.position[1] += self.move_vals[1]
        #note, the position does NOT stop when it passes the target, nor when it goes offscreen. you have to make those checks yourself.


    #calculation method for how much each should move - DO NOT TOUCH
    @staticmethod
    def calc_move_vals(pointA:tuple,pointB:tuple,distance:float=None,speed:int=1) -> tuple: #calculating how much to move
        if type(distance) != float:
            distance=calc_distance(pointA,pointB)

        #preventing zero division
        if distance == 0:
            return (
            (speed * (pointB[0] - pointA[0]) ),
            (speed * (pointB[1] - pointA[1]) )
        )

        #normal movement calc
        return (
            (speed * (pointB[0] - pointA[0]) / distance),
            (speed * (pointB[1] - pointA[1]) / distance)
        )
    #calculation method for distance - DO NOT TOUCH
    @staticmethod
    def calc_distance(pointA:tuple,pointB:tuple): #calculating distance, self explanatory
        return sqrt(
                ((pointB[0]-pointA[0])**2) + 
                ((pointB[1]-pointA[1])**2)
            ) 


##EXAMPLE CODE - COMMENT THIS OUT ON IMPLEMENTATION PLEASE. IT IS UNNECESSARY TO HAVE IT LOADED INTO MEMORY
class SampleBullet():
    #initialization
    def __init__(self,position,target):
        self.position = position
        self.target = target
        self.movement = MovingPoint(self.position,self.target,speed=1)
    #updating
    def update(self):
        self.movement.update()
        self.position = self.movement.position

#RUNNING THE EXAMPLE
bullet=SampleBullet((0,0),(99,77))
print(bullet.movement.pointA,bullet.movement.pointB,'\n@@@@@@@@@@@@@@@@@@@@@@@@@')
for i in range(150):
    bullet.update()
    print(round(bullet.position[0],3),round(bullet.position[1],3)) #note how this is ROUNDED. This goes to roughly a DOZEN DIGITS
print('@@@@@@@@@@@@@@@@@@@@@@@@@\n',bullet.position,bullet.movement.pointB)


