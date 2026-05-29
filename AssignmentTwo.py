#Ques. 1
# PIN = 1234
# pin = int(input("Enter Pin:"))
# balance = int(input("Enter Your Current Balance:"))
# withdrawal = int(input("Enter your withdrawal amount:"))

# if PIN != pin:
#     print("PIN is incorrect")
# else:
#     if balance < withdrawal:
#         print("Insufficient balance")
#     elif withdrawal % 100 != 0:
#         print("Invalid amount! Amount should be multiple of 100")
#     else:
#         print("Withdrawal successful")
#         print("Remaining Amount",balance - withdrawal)


#Ques. 2
# year = int(input("Enter Year:"))
# month = int(input("Enter month between 1 and 12:"))
# leap = False
# #Lear year logic
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     leap = True

# if month == 2:
#     if leap:
#         days = 29
#     else:
#         days = 28
# elif month in [1,3,5,7,8,10,12]:
#     days = 31
# elif month in [4,6,9,11]:
#     days = 30
# else:
#     days = "Invalid month"
# print(days)


# Ques. 3

# num1 = int(input("Enter num1:"))
# num2 = int(input("Enter num2:"))

# add = num1 + num2
# print("Addition:",add)

# subtract = num1 - num2
# print("Subtraction:",subtract)

# mul = num1 * num2
# print("Multiply:",mul)

# div = num1 / num2
# print("Division:",div)

# modulo = num1 % num2
# print("Modulus:",modulo)

#Ques. 4

# initialList = [x for x in range(1,21)]
# print(initialList)

# finalList = [x ** 2 for x in range(1,21)]
# print(finalList)

#Ques. 5
# student = {
#     'OM' : 98,
#     'Kushagra' : 97,
#     'Anupam' : 96,
#     'Yatin' : 99,
#     'Nikhil' : 95
# }

# print(student.keys())
# print(student['OM'])

# highest = max(student,key=student.get)
# print('Highest Marks:',student[highest])

# student['Rahul'] = 100
# print(student)

#Ques. 6

# student = {
#     'Name' : 'Nikhil',
#     'Age' : 20,
#     'Course' : 'Data Science with AI & ML'
# }

# set1 = set(x for x in range(1,6))

# inp = input("Enter number:")
# num = int(inp)

# print(student)
# print(set1)
# print(num)
# print(type(num))



