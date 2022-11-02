from tkinter import Y


def fn4():
    z = x + y
    print(z)

def fn5():
    x = 5
    y = 3
    z = x + y
    print(z)

x = y = z = 5
print(x, y, z)
fn4()
print(x, y, z)
fn5()
print(x, y, z)
