#Andrew Church
#Adam Walker
#Programming assignment 1

while True:
    #Asks for input
    shape=input('square, rectangle, circle, or triangle? ')
    #Square area
    if shape=="square":
        length=input("how long is one side of your square? ")
        print("Your square is " + str(int(length)**2) + " square units!")
        del length
    #Rectangle area
    elif shape=="rectangle":
        length=input("what is the length of your rectangle? ")
        width=input("what is the width of your rectangle? ")
        print("Your rectangle is " + str(int(length)*int(width)) + " square units!")
        del length
        del width
    #Triangle area
    elif shape=="triangle":
        length=input("what is the length of your triangle? ")
        width=input("what is the width of your triangle? ")
        print("Your rectangle is " + str(int(length)*int(width)*0.5) + " square units!")
        del length
        del width
    #Circle area
    elif shape=="circle":
        radius=input("What is the radius of your circle? ")
        print("Your circle is " + str(3.14*int(radius)**2) + " square units!")
        del radius
    #Else
    else:
        print("PUT THE SHAPES I REQUESTED YOU DINGBAT")
    continue