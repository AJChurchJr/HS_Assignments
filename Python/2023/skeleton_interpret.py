"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""

#Complete the following skeleton code as indicated by the comments for each function.. You should remove my comments. You should also add an appropriate program header. You may need to change the parameters in the functions. You may NOT have any global variables in your program.
#The program stores a list of Olympic athletes and scores for different events. (The data is completely fabricated). Each athlete is represented as a list containing the athlete's name, the country for which the athlete is competing and a set of scores. The initial data will look like this:
#athletes = [["Madeline Schizas", "CAN", 8.2, 9.3, 8.8, 9.0],
#                ["Yi Zhu", "CHN", 9.0, 8.8, 9.3],
#                ["Jin Boyang", "CHN", 9.1, 9,8, 9.5]]
#You will write functions that perform actions on this data set such as finding the highest average scoring athlete(s), adding an athlete etc.
#This looks challenging and may feel overwhelming. If you work at it one function at a time, you will feel less overwhelmed. There is a lot of information in the comments of each function -- be sure to read it!
   
def printScore(athleteName, scoreNumber, athleteData = None) -> None:
    #hahahaha i have bested you mister krueger
    #i changed the list so it DOES work
    if athleteName not in athleteData.keys():
        print("NAME NOT IN DATA SET")
        return

    #given the list of athletes, an athlete's
    #name, and an integer indicating which score to print.
    #for instance, to print the athlete's first score, scoreNumber =1
    #print the athlete's name, their country, and the score on the event indicated by scoreNumber

    #checking out of bounds
    elif scoreNumber > (len(athleteData[athleteName][1])-1):
        print("SCORE NUMBER OUT OF RANGE")
        return

    #printing if no errors tripped
    else:
        print(athleteData[athleteName][1][scoreNumber])

   #optional return
    return athleteData[athleteName][1][scoreNumber]



def totalScore(data):
    total = 0
    for i in range(len(data[1])): #data[1] contains the scores in a list
        total += data[1][i]
    return total

def avgScore(data,total = None):
    if total is None:
        total = 0
        for i in range(len(data[1])): #data[1] contains the scores in a list
            total += data[1][i]
        return(total/len(data[1]))
    else:
        return(total/len(data[1]))
    


    
def highestAverageScore(athleteData):
    #values
    averages={}
    highest = 0
    name = ""

    #figuring out all averages
    for key,value in athleteData.items():
        averages[key] = avgScore(athleteData[key])

    #iterating through every item in list
    for key,value in averages.items():
        if value > highest:
            #updating highest values
            highest = value
            name = key

    return name



def increaseScores(athleteData, country):
    #iterating through athletes
    for value in athleteData.values():
        #checking valid country
        if value[0] == country:
            #iterating through scores
            for _ in range(len(value[1])):
                #checking score
                if value[1][_] + 0.3 <= 10.0:
                    #scoring
                    value[1][_] += 0.3



def addNewAthlete(athleteData):
    #input
    name = input("enter name:")
    #input validation
    if name in athleteData.keys():
        print("name already exists")
        return 

    country = input("enter country:")
    
    scores = input("enter scores divided by commas").split(",")
    #input validation
    for i in range(scores):
        try:
            scores[i] = int(scores[i])
        except:
            print("non-number entered")
            return

    #ouptut
    athleteData[name] = [country,scores]



def main():

    #we will start with two athletes in our list.
    athletes = {
        "Madeline Schizas": ["CAN", [8.2, 9.3, 8.8, 9.0] ],
        "Yi Zhu": ["CHN", [9.0, 8.8, 9.3] ],
        "Jin Boyang": ["CHN", [9.1, 9,8, 9.5] ],
        }
    
    print("Here is the data set\n"+ str(athletes))

    #printing scores
    print("---SCORES---")
    printScore("Madeline Schizas",2,athletes)
    printScore("Yi Zhu",1,athletes)
    printScore("Andrew Church",2,athletes)


    #allow the user to add a new athlete.
    print("---I AM FORCING YOU TO MAKE A NEW ATHLETE---")
    

    #show the total score for Yi Zhu
    print("---YI ZHU TOTAL SCORE---")
    print(totalScore(athletes["Yi Zhu"]))

    #increase all the scores for all athletes from China (CHN) and Canada (CAN)
    print("---INCREASING CHINESE SCORES---")
    increaseScores(athletes,"CHN")
    print(athletes)
    print("---INCREASING CANADIAN SCORES---")
    increaseScores(athletes,"CAN")
    print(athletes)

    #find (and display) the names of the highest average scoring athletes
    print("---HIGHEST SCORING ATHLETES---")
    print(highestAverageScore(athletes))
    

   
    
    
main()   

"""OUTPUTS


too many outputs idk what to even do here
"""
