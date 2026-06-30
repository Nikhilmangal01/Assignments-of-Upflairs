Question 1

Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification and regression tasks. It is mainly used for classification problems.
The main objective of SVM is to find the best boundary (hyperplane) that separates different classes with the maximum possible margin.

Working Principle of SVM:
Import the training dataset.
Identify the classes in the dataset.
Find the optimal hyperplane that separates the classes.
Maximize the distance (margin) between the hyperplane and the nearest data points.
These nearest data points are called support vectors.
When a new data point is given, SVM checks on which side of the hyperplane it lies and predicts its class.

Question 2

Hyperplane

A hyperplane is the decision boundary that separates two classes.

In 2D, it is a line.
In 3D, it is a plane.
In higher dimensions, it is called a hyperplane.
Example

Suppose students are classified as:

Pass (1)
Fail (0)

An SVM draws a line that best separates Pass and Fail students.

Support Vectors

Support vectors are the closest data points to the hyperplane.

They are important because:

They determine the position of the hyperplane.
Removing other points usually does not change the boundary.
Removing support vectors changes the decision boundary.

Question 3

(a) Linear SVM vs Non-Linear SVM
Linear SVM	Non-Linear SVM
Used when data is linearly separable	Used when data is not linearly separable
Uses a straight line/hyperplane	Uses curved decision boundaries
Faster	Slower
Simpler	More complex

(b) Kernel Functions in SVM

A kernel function helps SVM classify data that is not linearly separable by mapping it into a higher-dimensional space.

Common kernels:
Linear Kernel – For linearly separable data.
Polynomial Kernel – Creates polynomial boundaries.
RBF (Radial Basis Function) – Most commonly used for complex data.
Sigmoid Kernel – Similar to neural networks.

Question 4

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


data = {
    "Study Hours": [1,2,3,4,5,6],
    "Attendance": [50,55,60,70,75,85],
    "Result": [0,0,0,1,1,1]
}

df = pd.DataFrame(data)

print(df)


X = df[["Study Hours","Attendance"]]
y = df["Result"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)


model = SVC(kernel="linear")

model.fit(X_train, y_train)


prediction = model.predict([[4.5,72]])

print("Predicted Result:", prediction)


y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))


Question 5

import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

data = {
    "Weight": [120,130,150,170,180,200],
    "Size": [6,6.5,7,8,8.5,9],
    "Fruit": ["Apple","Apple","Apple","Orange","Orange","Orange"]
}

df = pd.DataFrame(data)

print(df)


encoder = LabelEncoder()

df["Fruit"] = encoder.fit_transform(df["Fruit"])


X = df[["Weight","Size"]]
y = df["Fruit"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)


model = SVC(kernel="linear")

model.fit(X_train, y_train)

# Prediction
prediction = model.predict([[160,7.5]])

print("Predicted Fruit:")
print(encoder.inverse_transform(prediction))


y_pred = model.predict(X_test)

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))


print("\nClassification Report")
print(classification_report(y_test, y_pred))
