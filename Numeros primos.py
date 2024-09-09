aux1 = 0 
j = 1000

while aux1 < 10: 
    aux2 = 0
    if j % 2 == 0: # modulo
        j += 1
    else: 
        i = 3 
        while i < j : 
            if j % i == 0:
                aux2 += 1
                i += 1
            else:
                i+= 1
        if aux2 == 0:
            print(f"{j} es primo")
            aux1 += 1
            j += 1
        else:
            j += 1
print("Gracias por usarme y dejarme")
