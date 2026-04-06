with open("ListOfPuzzles.csv","r") as CSV:
    raw = CSV.read().split('\n')
#each line here has the category and the phrase, separated by a pipe.
parsed=""
parsed_cat=""

for i in range(len(raw)):
    for j in range(len(raw[i])):
        if raw[i][j] == "|":
            parsed+=raw[i][j+1:]+","
            parsed_cat+=(raw[i][:j])+","

       


with open("ListOfPuzzles.txt","w+") as NEW:
    NEW.write(parsed)
with open("ListOfPuzzlesCAT.txt","w+") as NEW:
    NEW.write(parsed_cat)

input('done')

