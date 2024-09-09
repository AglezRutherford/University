print("""
                  _..-----._
                  .'          '.
                 /              \\
                |                ;
                |                 |
                \                 |
                 \               ;
           _..----'             /
         .`-. .-'``'-.       .-'
       .'_   `  _     '.    `'.
      /  _`    _ `      \      \     _...._
   _  | /  \  /  \      |       | .-'      `'.
  / \ | | /|  | /|      |       ;'            \\
 |  |_\ \_|/  \_|/      /                      ;
 .\_/  `'-.            /_...._                 |
/          `                  `\               |
|                        __     |             /
 \                       / `   //'.         .'
  '._                  .'     .'   `'-...-'`
     `"'-.,__    ___.-'    .-'
    jgs  `-._````  __..--'`
             ``````
      """)
print("""
  Este programa juega fizzBuzz. Las reglas son simples: si un numero
  entero es divisible entre 3 entonces se escribe 'Fizz', si es divisible 
  entre 5 se escribe 'buzz' y si es divisible entre ambos se escribe 'FizzBuzz'.        
""")

nlim = int(input('Dame un numero o limite:  '))
for i in range(1,nlim+1):
    if (1 % 3 == 0 and i % 5 == 0):
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)