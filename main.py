#XCSR Backend
#Handles  creation of entries
#Save entry to CSV. HTML page should read the CSV file.
import re
import csv
import datetime #Currently unused.

#f = open('/home/pj/Documents/test.csv','r+')
#csv_f = csv.reader(f)

newGamer = ['hello','egghole','ehole99','19:20']
def addItem(newItem):
    addValue = 1 #Changes to one if adding an entry to the bottom of the list.
    newItemLst = newItem #Save item to list
    newItem = ','.join(newItem) #Remove list artifacts, convert to string
    csvf = open('times.csv','r+')
    csv_f = csv.reader(csvf)
    minute= int(newItemLst[3][0:2])
    second= int(newItemLst[3][3:5])
    fusedTime = int(str(minute)+str(second))
    print(f'Fused Time: {fusedTime}')

    for row in csv_f:
        rowMin = int(row[3][0:2])
        rowSec = int(row[3][3:5])
        fusedRowTime = int(str(rowMin)+str(rowSec)) #Used to compare second-based times
        print(f'Fused Row Time: {fusedRowTime}')
        print(row)
        if fusedRowTime > fusedTime:
            print('Greater')
            name = row
            addValue = 0
            break
        else:
            print('Else')
            name = row

    rowStr = ','.join(name)
    #print(f'Name: {name}')
    with open('times.csv','r+') as f:
        a = [x.rstrip() for x in f]
        index = 0
        for i in a:
            if i.startswith(str(rowStr)):
                a.insert(index + addValue,newItem)
                break
            index +=1
        f.seek(0)
        f.truncate()
        for line in a:
            f.write(line + '\n')
    print(f'Add Value: {addValue}')
    print(f'Index: {index}')
    print(str(rowStr))
addItem(newGamer)