print("Ingrese la fecha menor en el siguiente formado  (Ejemplo: DD MM AAAA)")
d1 = int(input("DD:"))
m1 = int(input("MM:"))
a1 = int(input("AAAA:"))
print("Ingrese la fecha mayor en el siguiente formado (Ejemplo: DD MM AAAA)")
d2 = int(input("DD:"))
m2 = int(input("MM:"))
a2 = int(input("AAAA:"))

# Calculamos dias desde el inicio del calendario hasta la primera fecha
dias1 = 0 
for i in range(1,a1+1):
    if (i % 400 == 0):
        dias1 = dias1 + 366
    elif (i % 4 == 0) and (i % 100 != 0):
        dias1 += 366
    else :
        dias1 += 365

for i in range(1,m1+1) :
    if (i == 1 or i == 3 or i == 5 or i ==7 or i == 8 or i == 10 or i == 12):
        dias1 += 31
    elif (i == 4 or i == 6 or i == 9 or i == 11):
        dias1 += 30
    if (i == 2):
        if (a1 % 400 == 0):
            dias1 += 29
        elif (a1 % 4 == 0) and (a1 % 100 != 0):
            dias1 += 29
        else: 
            dias1 += 28

dias1 += d1

# Calculamos dias desde el inicio del calendario hasta la segunda fecha
dias2 = 0 
for i in range(1,a2+1):
    if (i % 400 == 0):
        dias2 = dias2 + 366
    elif (i % 4 == 0) and (i % 100 != 0):
        dias2 += 366
    else :
        dias2 += 365

for i in range(1,m2+1) :
    if (i == 1 or i == 3 or i == 5 or i ==7 or i == 8 or i == 10 or i == 12):
        dias2 += 31
    elif (i == 4 or i == 6 or i == 9 or i == 11):
        dias2 += 30
    if (i == 2):
        if (a2 % 400 == 0):
            dias2 += 29
        elif (a2 % 4 == 0) and (a2 % 100 != 0):
            dias2 += 29
        else: 
            dias2 += 28

dias2 += d2

# Calculamos la diferencia en dias
dif = abs(dias2 - dias1)

print(f"Los dias de diferencia son los siguientes: {dif}")