#!/usr/bin/python

import pickle
import numpy
import sys
import matplotlib.pyplot
from sklearn import linear_model
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from outlier_cleaner import sortByError

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)
trainX = list(map((lambda x: x[0]), data))
trainY = list(map((lambda x: x[1]), data))

l = len(trainX)
trainX = numpy.array(trainX)
trainY = numpy.array(trainY)
trainX = trainX.reshape(l,1)
trainY = trainY.reshape(l,1)
### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

reg = linear_model.LinearRegression()
reg.fit(trainX, trainY)
predictions = reg.predict(trainX)
sort_data = sortByError( predictions, trainX, trainY )


print(sort_data[len(sort_data) - 1])
l = sort_data[len(sort_data) - 1][3] + 1
for x in data_dict:
    l = l -1
    print(x)
    print(l)
    if l == 0:
        break
