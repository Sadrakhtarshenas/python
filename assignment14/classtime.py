class Time:
    def __init__(self, ho, me, se, ho2, me2, se2):
        self.h = ho
        self.m = me
        self.s = se
        self.h2 = ho2
        self.m2 = me2
        self.s2 = se2
    def sum(self):
        hous = self.h + self.h2
        minuts = self.m + self.m2
        seconds = self.s + self.s2
        while not(0 <= seconds <= 60 and 0 <= minuts <= 60):
            if seconds >= 60:
                seconds -= ((seconds // 60) * 60)
                minuts += (seconds // 60)
            if minuts >= 60:
                minuts -= ((minuts // 60) * 60)
                hours += (minuts // 60)
        print(str(hours) + ":" + str(minuts)  + ":" + str(seconds))
    def sub(self):
        hour_m = self.h - self.h2
        minut_m = self.m - self.m2
        second_m = self.s - self.s2
        while not(0 <= second_m <= 60 and 0 <= minut_m <= 60):
            if second_m < 0:
                minut_m -= 1
                second_m += 60
            if minut_m < 0:
                hour_m -= 1
                minut_m += 60
        print(str(hour_m) + ":" + str(minut_m)  + ":" + str(second_m))
t = input("enter time1:for exampel (20:45:30)\n")
t2 = input("enter time2:for exampel (20:45:30)\n")
op = int(input("1_sub\n2_sum\nenter number of your choice: "))
t = t.split(":")
t = [eval(i) for i in t]
t2 = t2.split(":")
t2 = [eval(i) for i in t2]
time = Time(t[0], t[1], t[2], t2[0], t2[1], t2[2])
if op == 1:
    time.sub()
else:
    print()