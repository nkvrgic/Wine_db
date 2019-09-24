import pandas
import csv
from array import *
import numpy


#Import read/write files & data
winemagdata ="winemag-data_first150k.csv"
names1 = ['1','2','3','4','5','6','7','8','9','10']
winemagdataset = pandas.read_csv(winemagdata, names=names1)

wine_db = "Wine_db.csv"
names2 = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
wine_dbdataset = pandas.read_csv(wine_db, names=names2)

#Construct 2D Data Arrays
in_ar = winemagdataset.values
out_ar = wine_dbdataset.values
print(out_ar)

#Gather All Specified Varietals
varietals = [row[0] for row in out_ar]

#Gather All Specified Notes
notes=[]
i = 8
while i<13:
    for x in out_ar[1:,i]:
        if x.lower() not in notes:
            notes.append(x.lower())
    i=i+1

#Read in_ar LBL
descriptions = [x[1] for x in in_ar]
print(len(descriptions))

outfile = "managerout2.txt"
#Check Description for Notes
i=0
with open(outfile, 'w',encoding="utf-8") as fd:
    for entry in descriptions:
        caught=[]
        for x in notes:
           if x in entry:
               caught.append(x)
        while len(caught)<5:
            caught.append(" ")
        tempar= str(str(in_ar[i][8])+','+'0'+','+'0'+','+'0'+','+'0'+','+'0'+','+"null"+','+"null"+','+str(caught[0])+','+str(caught[1])+','+str(caught[2])+','+str(caught[3])+','+str(caught[4])+"\n")
        if str(in_ar[i][8]) in varietals:
            fd.write(tempar)
        i=i+1
    fd.close()
with open('flavours2.txt', 'w',encoding="utf-8") as fc:
    for x in notes:
        fc.write(x+'\n')




