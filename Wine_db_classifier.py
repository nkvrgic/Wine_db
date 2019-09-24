
# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB


dataurl = "winemag_clean.csv"
names = ['varietal','note1','note2','note3','note4','note5']
dataset = pandas.read_csv(dataurl)

print(dataset.shape, '\n')
print(dataset.head(10), '\n')
print(dataset.describe(), '\n')


#Create validation set
array = dataset.values
x = array[:,0:5]
y = array[:,5]
val_size = 0.2
seed = 7
scoring = 'accuracy'
x_train, x_validation, y_train, y_validation = model_selection.train_test_split(x,y,test_size=val_size, random_state=seed)
model = GaussianNB()
model.fit(x_train, y_train)
predictions = model.predict(x_validation)
print(accuracy_score(y_validation, predictions))
print(confusion_matrix(y_validation, predictions))
print(classification_report(y_validation, predictions))

