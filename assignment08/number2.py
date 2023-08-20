number = int(input("enter youre number:\n")) # 5

for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
"""
out put:
1
12
123
1234
12345
"""

for i in range(number, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
'''
out put:
12345
1234
123
12
1
'''



'''
out put:
54321
4321
321
21
1
'''