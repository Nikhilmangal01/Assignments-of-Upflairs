# 1. Write a function that accepts student details using **kwargs and prints them. 

# def func(**kwargs):
#     for key,value in kwargs.items():
#         print(f'{key} : {value}')

# func(Name='NIKHIL',Age=20)

# 2. Write a recursive function to find factorial of a number. 

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)

# a = int(input("ENTER A:"))
# print(f'THE FACTORIAL FOR {a} IS:',fact(a))

# 3. Write a program to: ● Create a file  ● Write data into it  ● Read and display the content 

# with open('file.txt','w') as f:
#     f.write('HELLO MY NAME IS NIKHIL!\n')
#     f.write('MY AGE IS 20')

# with open('file.txt','r') as f:
#     print(f.read())

# 4. Create a dictionary and store it in a JSON file. Then read and print it. 

# mydict = {
#     'Name' : 'NIKHIL MANGAL',
#     'Age' : 20,
#     'City' : 'JAIPUR'
# }

# import json

# with open('Practice.json','w') as f:
#     json.dump(mydict,f)
# with open('Practice.json','r') as f:
#     print(json.load(f))


# 5. Write a program to handle division by zero using try-except-finally. 

# a = int(input("A: "))
# b = int(input("B:"))

# try:
#     c = a/b
# except ZeroDivisionError:
#     print("NUMBER DIVIDED BY 0")
# except:
#     print('ERROR OCCURED')