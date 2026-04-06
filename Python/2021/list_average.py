def calculateAverageSpeed(speedlist):
    totalspeed = 0
    try:
        for item in speedlist:
            totalspeed+=item
    except:
        print('You input something that was not a number')
    AvgSpd=totalspeed/len(speedlist)
    return AvgSpd
print(calculateAverageSpeed([1,2,3,4,5,6,7,8,9,10]))
print(calculateAverageSpeed([5,5,5,5,5]))
print(calculateAverageSpeed([122432535235,2345234523452784582745,24527453285932469593257832496785932467985967854697826934566245643296,845734873490583592487285744857398457324934258732349857324582759823745]))