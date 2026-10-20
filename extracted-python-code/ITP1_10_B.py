##S: Area of the triangle
##L: The length of the circumference of the triangle
##h: The height of the triangle with side a as a bottom edge
import math

a, b, c = map(int, input().split())
s = a * b * math.sin(math.radians(c)) / 2
l = a + b + math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(c)))
h = 2 * s / a
print("{:.4f}".format(s))
print("{:.4f}".format(l))
print("{:.4f}".format(h))

