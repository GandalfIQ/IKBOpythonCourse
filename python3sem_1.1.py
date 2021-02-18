import math
x = float(input())
y = float(input())
z = float(input())
res = ((y**4 +math.sin(x))/(math.tan(z**4)-abs(z))-(math.sqrt((z**4+5*x**7)/(abs(z)-math.e**y)))+math.tan(z)+2*z**5-46)
print("{:.2e}".format(res))