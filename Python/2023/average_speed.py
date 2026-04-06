"""ANDREW CHURCH -- ALLEN KRUEGER -- CIS AM"""

def avg_spd(uphill_mph=None,uphill_time=None,downhill_mph=None):
    #uphill rates
    if uphill_time == None: uphill_time = int(input("uphill time (mins):"))
    if uphill_mph == None: uphill_mph = int(input("uphill mph:"))

    #distance based off uphill
    distance = (uphill_time/60)*uphill_mph #distance in miles

    #downhill rates
    if downhill_mph == None: downhill_mph = int(input("downhill mph (mins):"))
    downhill_time = distance/downhill_mph * 60

    #calculating averages
    uphill_percent = uphill_time/(uphill_time+downhill_time)
    downhill_percent = downhill_time/(uphill_time+downhill_time)

    avg = (
        (uphill_mph * uphill_percent) +
        (downhill_mph * downhill_percent)
        )

    print("Your average MPH is:",str(avg))
    return avg

avg_spd()

"""OUTPUTS:
18,20,60 -> 30.0
36,40,120 -> 60.0
1,2,3 -> 2.4000000000000004
4,4,4 - > 4.0 
"""

