#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 


clf = DecisionTreeClassifier(random_state=0)
a_train, a_test, b_train, b_test = train_test_split(features, labels, test_size=0.3, random_state=42)
clf.fit(a_train, b_train)
result = clf.predict(a_test)
l = len(result)
cnt = 0
for i in range(l):
  if result[i] == 1 and b_test[i] == 0:
    cnt += 1
print cnt
