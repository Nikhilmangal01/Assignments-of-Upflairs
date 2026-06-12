# Pandas is an open-source Python library used for data manipulation and analysis. It provides powerful data structures such as Series and DataFrame for handling structured data efficiently.

# Role in Data Analysis

# Reading data from CSV, Excel, JSON, SQL, etc.
# Cleaning and preprocessing data.
# Handling missing values.
# Filtering and sorting data.
# Performing statistical analysis.
# Data aggregation and transformation.


# Role in Machine Learning

# Preparing datasets before training models.
# Feature selection and feature engineering.
# Handling missing values and duplicates.
# Converting raw data into a suitable format for ML algorithms.
    



# 2. Differentiate Between
# (a) Series vs DataFrame


# | Feature   | Series            | DataFrame                |
# | --------- | ----------------- | ------------------------ |
# | Dimension | 1-Dimensional     | 2-Dimensional            |
# | Structure | Single column     | Multiple columns         |
# | Index     | Has index         | Has rows and columns     |
# | Example   | Marks of students | Complete student dataset |

# (b) loc[] vs iloc[]

# | loc[]                    | iloc[]                      |
# | ------------------------ | --------------------------- |
# | Access data using labels | Access data using positions |
# | Uses row/column names    | Uses row/column numbers     |
# | Inclusive slicing        | Exclusive slicing           |


import pandas as pd

# data = {
#     "Name": ["Amit", "Neha", "Rahul", "Sneha"],
#     "Age": [20, 21, 19, 22],
#     "Marks": [85, 90, 78, 88]
# }

# df = pd.DataFrame(data)

# print("Original DataFrame:")
# print(df)


# print("\nFirst 2 Rows:")
# print(df.head(2))


# print("\nName and Marks:")
# print(df[["Name", "Marks"]])


# df["Result"] = ["Pass" if m >= 40 else "Fail"
#                 for m in df["Marks"]]

# print("\nDataFrame after adding Result:")
# print(df)

# print("\nStudents with Marks > 80:")
# print(df[df["Marks"] > 80])

# import numpy as np

# data = {
#     "Name": ["A", "B", "C", "D"],
#     "Age": [25, np.nan, 27, 24],
#     "Salary": [30000, 40000, np.nan, 35000]
# }

# df = pd.DataFrame(data)

# print("Original Dataset:")
# print(df)

# print("\nMissing Values:")
# print(df.isnull())

# avg_age = df["Age"].mean()
# df["Age"] = df["Age"].fillna(avg_age)

# med_salary = df["Salary"].median()
# df["Salary"] = df["Salary"].fillna(med_salary)

# print("\nCleaned Dataset:")
# print(df)


# df = pd.read_csv("Iris.csv")


# print(df.head())


# print("\nDataset Info:")
# df.info()


# print("\nShape of Dataset:")
# print(df.shape)


# print("\nAverage Sepal Length:")
# print(df["SepalLengthCm"].mean())


# print("\nSpecies:")
# print(df["Species"].unique())


# print("\nSummary Statistics:")
# print(df.describe())