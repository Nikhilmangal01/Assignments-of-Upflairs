A Decision Tree is a supervised machine learning algorithm used for classification and regression tasks. It works like a flowchart where:

Root Node: Represents the entire dataset.
Decision Node: Represents a feature used for splitting the data.
Leaf Node: Represents the final class label or prediction.

Working of Decision Tree:
  
Start with the entire dataset.
Select the best feature to split the data using criteria such as:
Entropy (Information Gain)
Divide the dataset into subsets.
Repeat the process until:
All records belong to the same class.
No further splitting is possible.
The leaf node gives the predicted class.


Question 2.

| Decision Tree      | Random Forest                            |
| ------------------ | ---------------------------------------- |
| Single tree model  | Collection of multiple decision trees    |
| Faster training    | Slightly slower                          |
| Can overfit easily | Less overfitting                         |
| Lower accuracy     | Higher accuracy                          |
| Easy to interpret  | Harder to interpret                      |
| Uses whole dataset | Uses random subsets of data and features |

Question 3.
Naive Bayes Classifier

Naive Bayes is a probabilistic supervised learning algorithm based on Bayes Theorem.

It assumes that all features are independent of each other.

It is widely used for:

Email Spam Detection
Sentiment Analysis
Text Classification
Document Classification

Question 4.

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB

df = pd.read_csv("email.csv")

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

le_x = LabelEncoder()
X.iloc[:, 0] = le_x.fit_transform(X.iloc[:, 0])

le_y = LabelEncoder()
y = le_y.fit_transform(y)

model = CategoricalNB()
model.fit(X, y)

test = pd.DataFrame({"Contains_Offer": ["Yes"]})
test.iloc[:, 0] = le_x.transform(test.iloc[:, 0])

prediction = model.predict(test)

print("Prediction:", le_y.inverse_transform(prediction)[0])


Question 5.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("iris.csv")

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

le = LabelEncoder()
y = le.fit_transform(y)
 
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
 
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("Predicted Species:")
print(le.inverse_transform(y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nAccuracy Score")
print(accuracy_score(y_test, y_pred))

Question 5.
      
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv("titanic.csv")


df["Age"].fillna(df["Age"].median(), inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)


le = LabelEncoder()

df["Sex"] = le.fit_transform(df["Sex"])
df["Embarked"] = le.fit_transform(df["Embarked"])


df.drop(["Name", "Ticket", "Cabin"], axis=1, inplace=True, errors="ignore")


X = df.iloc[:, 1:]      
y = df.iloc[:, 0]       

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy Score")
print(accuracy_score(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))
