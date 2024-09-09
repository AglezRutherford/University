import random
import sys 

print("Bienvenido al juego de piedra papel o tijera\n")
jugar_denuevo = True 
while jugar_denuevo:
 usuario = int(input('Elige (1) Piedra (2) Papel (3) Tijera: '))
 compu = random.randint(1,3)

 if usuario != 1 and usuario != 2 and usuario != 3 :
  print(f"Esto no existe\n {usuario}")
  sys.exit()

 opciones = ["Javiersolis", "Piedra", "Papel", "Tijera"]
 print(f'Elegiste: {opciones[usuario]}')
 print("vs")
 print(f'La computadora eligio: {opciones[compu]}')

 if usuario == 1 and compu == 2: 
     print('Perdiste')
 elif usuario == 1 and compu == 3:
     print('Ganaste')
 elif usuario == 2 and compu == 1:
     print('Ganaste')
 elif usuario == 2 and compu == 3:
     print('Perdiste')
 elif usuario == 3 and compu == 1:
     print('Perdiste')
 elif usuario == 3 and compu == 2:
     print('Ganaste')
 else:
     print('Empate')
 otravez = input('Quieres jugar de nuevo? (S) o (N): ')
 if otravez == "S" or otravez == "s" or otravez == "Si":
   jugar_denuevo == True
 else:
    jugar_denuevo = False


print("--- Fin del juego ---")
