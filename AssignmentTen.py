Question 1.

K-Nearest Neighbors (KNN) is a supervised machine learning algorithm used for classification and regression problems.
It predicts the output of a new data point based on the K nearest data points in the training dataset.

Working Process of KNN
Choose the value of K (number of nearest neighbors).
Calculate the distance between the new data point and all training data.
Select the K nearest neighbors.
For Classification:
Find the majority class among the K neighbors.
For Regression:
Calculate the average value of the K neighbors.
Return the predicted class/value.

Question 2.

The value of K determines how many nearest neighbors are considered while making predictions.

If K is Too Small (Example: K = 1)
Sensitive to noise
May overfit the training data
Prediction changes easily

Advantages
Captures local patterns

Disadvantages
High variance
Less accurate on noisy data

If K is Too Large
Uses many neighbors
May include points from different classes
Underfits the data

Advantages
Stable predictions
Less affected by noise

Disadvantages
Lower accuracy
Ignores local patterns

Question 3.

| KNN Classification      | KNN Regression              |
| ----------------------- | --------------------------- |
| Predicts categories     | Predicts continuous values  |
| Output is a class label | Output is a numerical value |
| Uses majority voting    | Uses average of neighbors   |

(b) Advantages of KNN
Simple and easy to understand
No training phase
Works for classification and regression
Good for small datasets
Easy to implement


(c) Disadvantages of KNN
Slow on large datasets
Sensitive to irrelevant features
Requires feature scaling
Choosing the correct K is difficult
High memory usage


Question 4.


import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


data = {
    "Study Hours": [1,2,3,4,5,6],
    "Attendance": [50,55,60,70,75,85],
    "Result": ["Fail","Fail","Fail","Pass","Pass","Pass"]
}

df = pd.DataFrame(data)

print(df)


encoder = LabelEncoder()
df["Result"] = encoder.fit_transform(df["Result"])

X = df[["Study Hours","Attendance"]]
y = df["Result"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)


model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)


prediction = model.predict([[4.5,72]])

print("Predicted Result:", encoder.inverse_transform(prediction))

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))


Question 5.


import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import (
    confusion_matrix,
    classification_report
)

# Dataset
data = {
    "Weight":[120,130,140,170,180,200],
    "Size":[6,6.5,7,8,8.5,9],
    "Fruit":["Apple","Apple","Apple","Orange","Orange","Orange"]
}

df = pd.DataFrame(data)

print(df)


encoder = LabelEncoder()
df["Fruit"] = encoder.fit_transform(df["Fruit"])

# Features and Target
X = df[["Weight","Size"]]
y = df["Fruit"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)


model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)


prediction = model.predict([[160,7.5]])

print("Predicted Fruit:")
print(encoder.inverse_transform(prediction))

y_pred = model.predict(X_test)


print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))


print("\nClassification Report")
print(classification_report(y_test, y_pred))

