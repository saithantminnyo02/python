import math as m
a , b = input("Enter length of two sides: ").split()
angle = input("Enter an angle between them: ")
if a.isnumeric() and b.isnumeric() and angle.isnumeric():
    a , b, angle = int(a) , int(b) , int(angle)
    angle = m.radians(angle)
    area = (a*b*m.sin(angle))/2
    print("The area of the triangle is %.2f"%area)
