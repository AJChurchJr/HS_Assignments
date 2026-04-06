"""ANDREW CHURCH -- ALLEN KRUEGER -- CIS AM"""
#write a list of six countries
#store it into the file
countries = ["United States", "Australia", "Britain"]
file = open("./test.txt","w")
for country in countries:
    file.write(str(country)+"\n")
file.close()
