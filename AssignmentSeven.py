
import numpy as np

#1.


# NumPy (Numerical Python) is a Python library used for numerical and scientific computing
# Applications in Machine Learning
# Data preprocessing
# Feature engineering
# Matrix operations
# Statistical analysis
# Model training and evaluation

# Importance of NumPy
# Fast Computation
# Memory Efficient
# Supports Multi-Dimensional Arrays
# Mathematical Operations
# Foundation of Data Science Libraries


#2.

# | Feature                 | Python List           | NumPy Array               |
# | ----------------------- | --------------------- | ------------------------- |
# | Speed                   | Slower                | Faster                    |
# | Memory Usage            | More                  | Less                      |
# | Mathematical Operations | Limited               | Directly Supported        |
# | Data Type               | Can store mixed types | Usually same type         |
# | Dimensions              | Nested lists required | Multi-dimensional support |


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# print(list1 + list2)


# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# print(arr1 + arr2)

# arr = np.arange(1, 11)

# print("1D Array:")
# print(arr)


# matrix = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# print("\n3x3 Matrix:")
# print(matrix)



# print("\nAddition:")
# print(matrix + matrix)

# print("\nMultiplication:")
# print(matrix * matrix)

# reshaped = arr.reshape(2, 5)

# print("\nReshaped Array (2x5):")
# print(reshaped)


# marks = np.array([45, 56, 67, 78, 89])

# print("Mean:", np.mean(marks))

# print("Median:", np.median(marks))

# print("Standard Deviation:", np.std(marks))

# print("Maximum:", np.max(marks))
# print("Minimum:", np.min(marks))

# print("Sorted Array:", np.sort(marks))




# arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

# print("First 4 Elements:")
# print(arr[:4])

# print("\nAlternate Elements:")
# print(arr[::2])

# print("\nReversed Array:")
# print(arr[::-1])


# arr[arr > 50] = 0

# print("\nAfter Replacement:")
# print(arr)