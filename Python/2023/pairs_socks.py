"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""

"""PSEUDOCODE
Given a list of integers representing the color of each sock, determine how many pairs of socks with matching colors there are. For example, there are 7 socks with colors [1, 2, 1, 2, 1, 3, 2]. There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.
Create a function that returns an integer representing the number of matching pairs of socks that are available.
Examples
sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]) ➞ 3
sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]) ➞ 4
sock_merchant([]) ➞ 0
"""

def sock_merchant(drawer=None):
    #taking input
    if drawer is None:
        drawer = input("Enter a list of numbers, separated by commas:").split(",")
    #input validation
    for i in range(len(drawer)):
        try: drawer[i] = int(drawer[i])
        except: drawer.pop(i)
    #sorting drawer / making values
    drawer.sort()
    pairs = 0
    i=0
    sock_count = {}

    for item in drawer:
        if item not in sock_count:
            sock_count[item] = 1
        else:
            sock_count[item] += 1

    for key,value in sock_count.items():
        pairs += value // 2

    return pairs
            
print(sock_merchant([1,1,2,2,3,4,3,4]))
print(sock_merchant([1,4]))
"""OUTPUTS
[1,1,2,2,3,4,3,4] -> 4
[1,1,2,2] -> 2
[1,2] -> 0
"""
