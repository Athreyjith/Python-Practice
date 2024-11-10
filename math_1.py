import math

x=9.1
print (math.pi)
print(math.e)
result = math.sqrt(x)
# result = math.ceil(x)            highest
result = math.floor(x)
print(result)



radius = float(input("enter the radius \t"))

circumference = 2*math.pi * radius

print(f" {round(circumference,2)}cm")



a = float(input("enter the value a"))
b = float(input ("enter the value b"))

c = math.sqrt(pow(a,2) + pow(b,2))
print(f"the c is {round(c,2)}")