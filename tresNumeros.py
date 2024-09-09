denuevo = True
while denuevo: 
     
 print("Ingrese tres numeros aleatorio/n")
 a =float(input("Ingresa un primer numero:"))
 b =float(input("Ingresa un segundo numero:"))
 c =float(input("Ingresa un tercer numero:"))

 if a < b :
     temp = a
     a = b
     b = temp
 if a < c :
     temp = a
     a = c
     c = temp
 if b < c :
     temp = b 
     b = c 
     c = temp
 print(f"Los numeros de mayor a menor son: {a},{b},{c}")
 otravez = input("Quieres volver a jugar? (s) o (n)")
 if otravez == "S" or otravez == "s" or otravez == "si" or otravez == "si" : 
     denuevo == True 
 else: 
    denuevo == False
     