import random
import matplotlib.pyplot as pp
b = input("Title of the graph : ")
c = input("Lable of x is : ")
d = input("Lable of y is : ")
print("Please enter the range for the graph")
a = input()
if a.isdigit():
    a = int(a)
else:
    print("enter a valid number for range next time")
    print("GoodBye!!")
    quit()
print("Please enter the values for x-axis")
x = []
for i in range(0 , a):
    ele = input()
    x.append(ele)
y = []
print("Please enter the values of the y-axis")
for i in range(0,a):
    ele =input()
    if ele.isdigit():
        ele = int(ele)
    else:
        print("enter valid value for the graph plotting next time. Goodbye!!!")
        quit()
    y.append(ele)
pp.plot(x,y)
pp.title(b)
pp.xlabel(c)
pp.ylabel(d)
pp.show()
print("Thank you for using this graph plotter.\nSee you again...")