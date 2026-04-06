"""ANDREW CHURCH -- ALLEN KRUEGER -- CIS AM"""
days=int(input("enter amount of days:"))
bonus=0
for i in range(days):
    if i+1 <= 32: pass
    elif i+1 >= 33 and i+1 <= 40: bonus += 325
    elif i+1 >= 41 and i+1 <= 48: bonus += 550
    elif i+1 > 48: bonus += 600

print(bonus)

"""OUTPUTS:
15: 0
38: 1625
50: 8200
"""
