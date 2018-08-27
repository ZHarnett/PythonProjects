from sklearn import tree, svm
from sklearn.linear_model import SGDClassifier

#[height(cm), weight(kg), shoe size(euro)]
X=[[181,80,44], [177,70,43], [160,60,38],[154,54,37],
    [166,65,40], [190,90,47], [175,64,39], [177, 70, 40], [159,59,38],
    [171,75,42], [181,85,43]]

Y=['male','female','female','female','male','male','male','female','male','female','male']

clf1 = tree.DecisionTreeClassifier()
clf1 = clf1.fit(X,Y)

clf2 = svm.SVC()
clf2.fit(X,Y)

clf3 = SGDClassifier()
clf3.fit(X,Y)

data = [[156,72,48]]

prediction1 = clf1.predict(data)
prediction2 = clf2.predict(data)
prediction3 = clf3.predict(data)

print(prediction1)
print(prediction2)
print(prediction3)
