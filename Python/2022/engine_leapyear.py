
import sys 

name=input('hello, who are you? ')
print('nice to meet you, ' + name + '!')
age= int(input('how old are you? '))
if age>100:
    print('You old damn dinosaur, go away and read the declaration of independence')
    sys.exit(0)
else:
    print('Oh, I see! Knowing that, you should turn 100 in aboutttt...' + str(100-age) + ' years!')
year= input('now, what year is it? ')
birthyear= int(year)-int(age)
if birthyear%4==0:
    if birthyear%100==0:
        if birthyear%400==0:
            print('you were born on a leapyear!')
        else:
            print('you were not born on a leapyear!')
    else:
        print('you were born on a leapyear!')
else:
    print('you were not born on a leapyear!')

input("Press enter to exit program")
