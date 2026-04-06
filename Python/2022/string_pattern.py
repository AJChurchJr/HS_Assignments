"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""
s=list(input("Enter a string:"))
p=list(input("Enter a pattern:"))
modified_s=s
match=True
for i in range(len(p)):
    
    #checks for a match
    if s[i]==p[i]:pass
    else:
        #checks for a question mark if not a match
        if p[i]=="?":
            pass
        #checks for an asterisk
        elif p[i]=="*":
            break_condition_met=False
            for j in range(i,len(s)):
                print(s[i],s[i+1],p[j])
                if p[i+1]==s[j]:
                    break_condition_met=True
                    break
            if not break_condition_met: match=False
        #trips the failsafe it is just not a match
        else:
            match=False
print(match)


"""OUTPUTS
This program does not work.
This is not a fair assignment.
This is not possible to make it work.
There is no way to make it recognize the pattern.
Random errors occur throughout that do not make any sense.
"""
