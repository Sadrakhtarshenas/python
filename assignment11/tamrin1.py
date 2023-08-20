# import math

# num1 = int(input())
# num2 = int(input())

# print("gcd: " , math.gcd(num1, num2))
# print("lcm: " , math.lcm(num1, num2))
def lcm(x, y):
   if x > y:
       lcm_ = x
   else:
       lcm_ = y

   while(True):
       if((lcm_ % x == 0) and (lcm_ % y == 0)):
           break
       lcm_ += 1

   return lcm_


num1 = float(input("enter your number: "))
num2 = float(input("enter your number: "))
print("lcm: ", lcm(num1, num2))