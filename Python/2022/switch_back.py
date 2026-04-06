"""ANDREW CHURCH -- ALLEN KRUEGER -- CIS AM -- 10/11/22"""

#divide text into "packets" the length of max_width
#put "packets" into a list
#every "packet" with an odd number index is reversed


#takes input
def iv(text):# makes an input statement and converts it to int with try-except
    while True:
        try:val=int(input(text));return val
        except: continue
text=input("Enter anything:");max_width=iv("How wide?");width=0;packets=[[]]

#figuring out how many lists to put into packets
for item in text:
    width+=1
    if width>=max_width:width=0;packets.append([])

#adding text into packets
packetIndex=0;width=0
for char in text:
    packets[packetIndex].append(char);width+=1
    if width>=max_width:width=0;packetIndex+=1

#reversing alternating packets
revPackets=[]
for i in range(len(packets)):
    if i%2!=0:
        newList=[]
        for j in range(len(packets[i])):newList.append(packets[i][len(packets[i])-(j+1)])
        revPackets.append(newList)
        
#putting reversed packets into the original list
packetIndex=0
for i in range(len(packets)): 
    if i%2!=0:
        packets[i]=revPackets[packetIndex]
        packetIndex+=1
        
#displaying final product
for packet in packets:
    for item in packet:print(item,end='')
    print('')
    
