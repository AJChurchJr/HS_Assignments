try:
    while True:
        y=int(input("YEAR:")) #year

        m=24 #Error shift for every 310 day period
        n=5 #cycle of days of the week in which the paschal moon occurs in that century
        a=y%19 #location of the year within the Metonic cycle
        b=y%4 #4-year cycle of leap years
        c=y%7 #Non-leap year is one day longer than 52 weeks
        d=((19*a)+m)%30 #Number of days that needed to be added to March 21
        e=((2*b)+(4*c)+(6*d)+n)%7 #days from the Paschal Full Moon to the next Sunday

        if y==1954 or y==1981 or y==2049 or y==2076:d-=7

        print("PASCHAL FULL MOON OCCURS",str(d),"DAYS AFTER MARCH 21")
        if (22+d)>31:print("PASCHAL FULL MOON OCCURS APRIL",str(22+d-31))
        else:print("PASCHAL FULL MOON OCCURS MARCH",str(22+d))
        
        print("EASTER SUNDAY SHOULD BE",str(22+d+e),"DAYS AFTER MARCH 21")
        if (22+d+e)>31:print("EASTER SUNDAY SHOULD BE APRIL",str(22+d+e-31))
        else:print("EASTER SUNDAY SHOULD BE MARCH",str(22+d+e))  

except:pass
