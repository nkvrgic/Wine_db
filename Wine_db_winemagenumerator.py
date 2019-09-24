# Load libraries
import numpy
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

f1 = "winemag_clean.csv"
f2 = "flavours_arr.txt"
data = open(f1, "r")
flav = open(f2, "r")
winemag_data = []
for i in data.readlines():
    winemag_data.append(i.split(","))
data.close()
print(winemag_data[8665])
flavours = []
for i in flav.readlines():
    j=i.split("\n")
    flavours.append(j[0])
flav.close()
print(flavours)
bigdata = []
outfile = "winemag_bow.txt"
with open(outfile,'w') as fd:
    for i in winemag_data:
        vector = [0]*len(flavours)
        vector.append(i[0])
        for j in flavours:
            if j in i:
                vector[flavours.index(j)] = 1
        #fd.write(str(vector))
        bigdata.append(vector)
print(bigdata[66958])
fd=open(outfile,'w')
for i in bigdata:
    for j in i:
        fd.write(str(j)+"\t")
fd.close()

array = numpy.array(bigdata)
x = array[:,0:5]
y = array[:,5]
val_size = 0.2
seed = 7
scoring = 'accuracy'
x_train, x_validation, y_train, y_validation = model_selection.train_test_split(x,y,test_size=val_size, random_state=seed)
model = LogisticRegression()
model.fit(x_train, y_train)
predictions = model.predict(x_validation)
print(accuracy_score(y_validation, predictions))
print(confusion_matrix(y_validation, predictions))
print(classification_report(y_validation, predictions))
    

    
    
