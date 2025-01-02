from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
iris=load_iris()
x,y=iris.data,iris.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)
clf=KNeighborsClassifier()
clf.fit(x_train,y_train)
accuracy = clf.score(x_test, y_test)
print(f"Accuracy = {accuracy:.2f}")
pred=clf.predict(x_test)
print("Misclassifications=",sum(y_test!=pred))

