x = float(input("Escribe el valor de x para calcular exp(x)"))

expx = 1.0
for i in range(1,100): #En py siempre hay que poner un rango en un mayor numero en el rango al que quiero llegar
    factorial = 1 
    for j in range(2, i+1):
        factorial *= j
    expx += x** i / factorial
print(f"El valor de exp({x}) es {expx}")