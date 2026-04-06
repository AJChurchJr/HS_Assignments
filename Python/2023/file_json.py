"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""
import json



############TESTING JSON -- CREDIT TO GEEKSFORGEEKS
###making a dictionary
##dictionary = {
##    "name":"jimmy",
##    "gpa":3.5,
##    "phone_num":1,
##}
##
###converting a dictionary to a json
##json_object = json.dumps(dictionary,indent=4)
##
##with open("test1.json","w") as file:
##    file.write(json_object)
##    #json.dump(dictionary,file) #Secondary method: json dump the original dict
##
##print(type(json_object))
####################################################


###########ACTUAL PROGRAM

#base dictionary
d = {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName':
'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly',
'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}

#converting to json
d_json = json.dumps(d,indent=4)

#writing
with open("test1.json","w") as file:
    file.write(d_json)


