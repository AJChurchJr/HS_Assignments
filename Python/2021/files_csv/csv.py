"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""
import os,json

def main(directory:str=("./")):
    #making values
    tables = {}

    #making dictionary keys for all csv files
    for _ in os.listdir(directory):
        if ".csv" in _:
            _=_.replace(".csv","") #removing extension
            tables[_] = {} #making key values




    #iterating through each file
    for _ in tables.keys():
        with open( directory+_+".csv","r") as f:  #f is file
            f=f.read()
            
            #converting csv to list of lists 
            f=f.split("\n")
            for i in range(len(f)):
                f[i]=f[i].split(",")

                
            #Now, technically I could leave this at that, however I think it would be nicer and more readable to convert the list into a dictionary
            #making headers the keys to the table's nested dictionary
            for i in range(len(f[0])): #f[0] is the header
                tables[_][f[0][i]] = [] #making nested dictionary keys
            header = f[0] #making a value for reference\
            del f[0]

            #adding values to list nested within a dictionary nested within a dictionary
            #iterating through each list within the csv file
            for i in range(len(f)):
                for j in range(len(f[i])):
                    tables[_][header[j]].append(f[i][j])

        
    del _,i,header,f,j #getting rid of temporary values      
        

    return tables


"""no output, as it varies depending on the file."""
if __name__ == "__main__":
    print(json.dumps(main("./"),indent=4))
