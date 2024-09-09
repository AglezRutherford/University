from math import sin, cos, cosh

print("Bienvenido a calcula-mesta")
x = float(input("Dame un numero real: "))
y = float(input("Dame otro numero real: "))

suma = x + y 
resta = x - y
producto = x * y
div = x / y
hola = sin(y)
xd = cosh(x)
print(f"La suma de {x}+{y} = {suma}")
print(f"La resta de {x}-{y} = {resta}")
print(f"El produco de {x}*{y} = {producto}")
print(f"La division de {x}/{y} = {div}")
print(f"El sin de {y} = {hola}")
print(f"El cosh de {x} = {xd}")