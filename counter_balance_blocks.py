
import csv
import itertools

# make a conditions file that contains x columns with all permutations of list

#a list of possible conditions
myList=['Fearful', 'Angry', 'Surprised', 'Neutral']

#get all permutations (of length 4)
allPerms = itertools.permutations(myList)

Shapes = "shapes"

# Create a list of dictionaries to turn into a conditions file
toCSV=[]
for thisPerm in allPerms:
    toCSV.append({'Cond1':Shapes, 'Cond2':thisPerm[0], 'Cond3': Shapes, 'Cond4':thisPerm[1], 'Cond5' : Shapes, 'Cond6':thisPerm[2], 'Cond7' : Shapes, 'Cond8':thisPerm[3], 'Cond9': Shapes})
#make a conditions file with keys as headers and values as rows
keys = toCSV[0].keys()
with open('conditions.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV)
