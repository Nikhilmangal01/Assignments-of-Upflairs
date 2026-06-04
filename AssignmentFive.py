############################################ Peterson Number ##############################################
# A = int(input("Enter A:"))
# def fact(n):
#     if n < 2:
#         return 1
#     else:
#         return n * fact(n-1)

# n = A
# sum = 0
# while n > 0:
#     tt = n % 10
#     sum = sum + fact(tt)
#     n //= 10

# if A == sum:
#     print("Peterson Number")
# else:
#     print("Not Peterson")


################################### Circular Prime Number #################################
# import math
# A = input("Enter A:")
# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2,math.sqrt(n)):
#         if n % i == 0:
#             return False
#     return True
# cp = True
# for i in range(len(A)):
#     rotation = int(A)

#     if not isPrime(rotation):
#         cp = False
#         break

#     A = A[1:] + A[0]

# if cp:
#     print("Circular Prime Number")
# else:
#     print("Not a Circular Prime Number")

############################################## Harshad Number #############################################

# A = int(input("ENTER A:"))
# n = A
# sum = 0
# while n > 0:
#     temp = n % 10
#     sum = sum + temp
#     n //= 10
# if A % sum == 0:
#     print("HARSHAD NUMBER")
# else:
#     print('NOT A HARSHAD NUMBER')


############################################## MAGIC NUMBER ##################################################
# A = int(input('ENTER A:'))
# while A > 9:
#     sum = 0
#     while A > 0:
#         sum += A % 10
#         A //= 10
#     A = sum

# if sum == 1:
#     print("Magic Number");
# else:
#     print("Not a Magic Number");


########################################### PASCAL TRIANGLE ##############################################  
# A = int(input('ENTER A:'))
# for i in range(A):
#     num = 1
#     for j in range(i+1):
#         print(num,end=" ")
#         num = num * (i-j)//(j+1)
#     print()

######################################### DUCK NUMBER ####################################################
# A = input('ENTER A:')
# isDuck = False
# for i in range(1,len(A)):
#     if A[i] == '0':
#         print("DUCK NUMBER")
#         isDuck = True
# if isDuck:
#     print("DUCK NUMBER")
# else:
#     print("NOT A DUCK NUMBER")

    



 