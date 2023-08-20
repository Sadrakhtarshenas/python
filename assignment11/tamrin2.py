# #factoreal
# number = int(input("please Enter integer number: "))
# if number < 0:
#     print("Sorry, factorial does not exist for negative numbers")
# else:
#     factorial = 1
#     for i in range(1, number+1):
#         factorial = factorial * i
# print("The factorial of {} is: {}".format(number, factorial))



# #fibonachi
# # Function for nth Fibonacci number 
# def Fibonacci(n): 
#     if n<0: 
#         print("Incorrect input") 
#     # First Fibonacci number is 0 
#     elif n==0: 
#         return 0
#     # Second Fibonacci number is 1 
#     elif n==1: 
#         return 1
#     else: 
#         return Fibonacci(n-1)+Fibonacci(n-2) 
# # Driver Program 
# print(Fibonacci(9))



#gcd

#Import math Library
import math 

#find the  the greatest  common divisor of the two integers
print (math.gcd(3, 6))
print (math.gcd(6,  12))
print (math.gcd(12, 36))
print (math.gcd(-12, -36))
print (math.gcd(5,  12))
print (math.gcd(10, 0))
print (math.gcd(0, 34))
print (math.gcd(0,  0))
