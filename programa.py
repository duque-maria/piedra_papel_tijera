import random

# input
print("························")
print("Piedra, papel o tijera")
print("························")

print("Opciones")
print("1. Piedra ")
print("2. Papel")
print("3. Tijera")

# input
usuario = int(input("Digite la opción (1, 2 o 3): "))

# processing
maq = random.randint(1,3)
if usuario < 1 or usuario > 4:
     print("Juegue nuevamente.")
     r = "Opción no válida."
else:
     # usuario escogió una opción válida
     if maq == 1:
          if usuario == 1:
               r= "Empate. Ambos han sacado Piedra."
          elif usuario == 2:
               r= "Ganaste. Has sacado papel y tu rival piedra"
          else: 
               r= "Perdiste. Has sacado tijeras y tu rival piedra"
     elif maq == 2:
          if usuario == 1:
               r= "Perdiste. Has sacado piedra y tu rival papel"
          elif usuario == 2: 
               r= "Empate. Ambos han sacado Papel."
          else:
               r= "Ganaste. Has sacado tijera y tu rival papel"
     else:
          if usuario == 1:
               r= "Ganaste. Has sacado piedra y tu rival tijera"
          elif usuario == 2:
               r= "Perdiste. Has sacado papel y tu rival tijera"
          else: 
               r= "Empate. Ambos han sacado Tijera"
# output
print("························")
print("Resultado")
print("····" + r + "···")
print("Usuario: " +str(usuario))
print("Máquina: " +str (maq))