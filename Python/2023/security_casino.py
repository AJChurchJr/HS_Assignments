"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""
"""
You're head of security at a casino that has money being stolen from it. You get the data in the form of strings and you have to set off an alarm if a thief is detected.
•	If there is no guard between thief and money, return "ALARM!"
•	If the money is protected, return "Safe"
String Components
•	x - Empty Space
•	T - Thief
•	G - Guard
•	$ - Money
Examples
security("xxxxTTxGxx$xxTxxx") ➞ "ALARM!"

security("xxTxxG$xxxx$xxxx") ➞ "Safe"

security("TTxxxx$xxGxx$Gxxx") ➞ "ALARM!"
"""

def thief_check(camera_raw = None):
    #input
    if camera_raw is None:
        camera_raw = input("What does the camera see?:")
    #input validation
    camera = []
    valid_list = ("T","G","$")
    for item in camera_raw:
        if item.upper() in valid_list:
            camera.append(item.upper())
    del valid_list, camera_raw
    #starting check
    tripped = False
    for i in range(len(camera)):
        #checking for thief 
        if camera[i] == "T":
            #checking for the ends/starts and if the thief is by the money
            if ((i != (len(camera)-1) and camera[i+1] == "$")
                or (i != 0 and camera[i-1] == "$")):
                tripped = True
    return tripped

print(thief_check("xxxxTTxGxx$xxTxxx"))
        
"""OUTPUTS
xxxxTTxGxx$xxTxxx -> True
xxTxxG$xxxx$xxxx -> False
TTxxxx$xxGxx$Gxxx -> True
"""
    

    
