import sys
try:
    x = int(input("X: "))
    y = int(input('Y: '))

except ValueError:
    print("Invalid type error")
    sys.exit()

try:
    z = x/y
except ZeroDivisionError:
    print("Divide by zero error")
    sys.exit()
print(z)
