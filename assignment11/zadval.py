from termcolor import colored

tol = int(input("enter tol: "))
arz = int(input("enter arz: "))
print(colored("x", "yellow"), sep="", end="\t")
for i in range(1, arz+1):
    print(colored(i, "red"), end="\t")
print()
for i in range(1, tol+1):
    print(colored(i, "blue"), end="\t", sep="")
    for j in range(1, arz+1):
        if i == j:
            print(colored((j * i), "blue"), end = "\t")
        else:
            print(j * i, end = "\t")

    print()