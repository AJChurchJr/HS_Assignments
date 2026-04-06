arguments=[]
print('give a number. keep giving numbers. when you are finished, input "done"')
while True:
    arg=input()
    if arg.lower() == 'done':
        break
    try:
        if int(arg) in arguments:
            print("number already in matrix")
            continue
        else:
            arguments.append(int(arg))
    except:
        print("error")
        continue

print(arguments)

def Matrix(arg):
    list = []
    for i in range(len(arguments)):
        list.append([])
        for x in range(len(arguments)):
            list[i].append((arguments[i], arguments[x]))
    return list


matrix = Matrix(arguments)
for list in matrix:
    print(list)