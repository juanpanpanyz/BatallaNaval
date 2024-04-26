import random
from typing import List

nCol: int = 10
nBarcos: int = int(input("Ingresen el numero de barcos que desean tener: "))
print( )
nDisparos: int = nBarcos * 2

# Crear el tablero para el jugador 1
listaF: List[List[bool]] = []
listaC: List[bool] = []
for i in range(nCol):
  for j in range(nCol):
    listaC.append(False)
  listaF.append(listaC)
  listaC = []


# Asignar barcos por usuario para jugador 1
print(f"El jugador 1, tiene {nBarcos} barcos")
for j in range(nBarcos):
  x = int (input(f"Ingrese la fila del barco {j+1}: "))
  y = int (input(f"Ingrese la columna del barco {j+1}: "))
  listaF[x][y] = True
  print( )

# Función para mostrar el tablero
def mostrar_tablero(tablero: List[List[bool]]) -> None:
    [print(" ".join("X" if celda else "-" for celda in fila)) for fila in tablero]

# Iniciar el juego
print("¡Bienvenido a Batalla Naval jugador 1!")
print(f"Tienes {nDisparos} disparos para hundir {nBarcos} barcos.\n")
mostrar_tablero(listaF)

disparos_acertados = 0
disparos_fallidos = 0

for _ in range(nDisparos):
    fila = int(input("\nIngrese la fila de su disparo (0-9): "))
    print( )
    columna = int(input("Ingrese la columna de su disparo (0-9): "))
    print( )

    if listaF[fila][columna]:
        print("¡Acertaste!")
        disparos_acertados += 1
        listaF[fila][columna] = False
    else:
        print("¡Fallaste!")
        disparos_fallidos += 1

    print(f"Disparos acertados: {disparos_acertados}, Disparos fallados: {disparos_fallidos}")
    mostrar_tablero(listaF)

    if disparos_acertados == nBarcos:
        print("\n¡Felicidades! ¡Hundiste todos los barcos!")
        break
else:
    print("\n¡Lo siento! Te has quedado sin disparos.")
