import random
from typing import List

# Definir la variable de las filas y columnas
nCol:int = 10
# Pedir el input al usuario de la cantidad de barcos
nBarcos: int = int(input(" Ingrese el numero de barcos con el que se desea jugar: "))
# Agarra el numero de barcos y lo duplica para conseguir el numero de disparos
nDisparos: int = nBarcos * 2

# Crear el tablero para el jugador 1 ListaC es las lista de las columnas y ListaF es las listas de las filas
listaFb: List[List[bool]] = []
for i in range(nCol):
  listaCb: List[bool] = [] 
  for j in range(nCol):
    listaCb.append(False)
  listaFb.append(listaCb)

# Crear el tablero para el jugador 2 ListaC es las lista de las columnas y ListaF es las listas de las filas
listaF: List[List[bool]] = []
for i in range(nCol):
  listaC: List[bool] = [] 
  for j in range(nCol):
    listaC.append(False)
  listaF.append(listaC)

print ("Jugador 1, es su turno de colocar sus barcos")
# Corre este codigo por la cantidad de barcos que haya 
for i in range(nBarcos):


    xb = int (input("\nIngrese la coordenada horizontal de 1 de su barco: "))
    yb = int (input("\nIngrese la coordenada vertical de 1 de su barco: "))
    listaF[xb][yb] = True
# Cambia el  valor false de las coordenadas dadas para uqe sea true (hay un barco)

print("Jugador 2, es turno de colcar sus barcos")
for i in range(nBarcos):

    xb = int (input("\nIngrese la coordenada horizontal de 1 de su barco: "))
    yb = int (input("\nIngrese la coordenada vertical de 1 de su barco: "))
    listaFb[xb][yb] = True

def mostrar_tablero(tablero: List[List[bool]]) -> None:
  [print(" ".join("X" if celda else "-" for celda in fila)) for fila in tablero]

# Iniciar el juego
print("¡Bienvenido a Batalla Naval! es el turno del Jugador 1 de disparar.")
print(f"Tienes {nDisparos} disparos para hundir {nBarcos} barcos.\n")
mostrar_tablero(listaF)

# Definimos las variables de los disparos que hace cada jugador
disparos_acertados = 0
disparos_fallados = 0
disparos_acertadosb = 0
disparos_falladosb = 0


 # Esto va a ocurrir mientras los dos jugadores tengan disparos y mientras no hayan acertado todos los barcos
while disparos_acertados < nBarcos and disparos_acertados + disparos_fallados < nDisparos and disparos_acertadosb < nBarcos and  disparos_acertadosb + disparos_falladosb < nDisparos:
  print ("\nAhora es el turno del jugador 1:")
  fila = int(input("\nIngrese la fila de su disparo (0-9): "))
  columna = int(input("Ingrese la columna de su disparo (0-9): "))

  if listaFb[fila][columna]:
      print("¡Acertaste!")
      disparos_acertados += 1
      listaFb[fila][columna] = False
  else:
      print("¡Fallaste!")
      disparos_fallados += 1

  print(f"Disparos acertados: {disparos_acertados}, Disparos fallados: {disparos_fallados}")


  print("Ahora es el turno del jugador 2 de disparar.")
  filab = int(input("\nIngrese la fila de su disparo (0-9): "))
  columnab = int(input("Ingrese la columna de su disparo (0-9): "))
#Se fija si la coordenada es true o flase, si es true entra al if
  if listaF[filab][columnab]:
        print("¡Acertaste!")
        disparos_acertadosb += 1
        listaF[filab][columnab] = False
  else:
        print("¡Fallaste!")
        disparos_falladosb += 1

  print(f"Disparos acertados: {disparos_acertadosb}, Disparos fallados: {disparos_falladosb}")
mostrar_tablero(listaF)
mostrar_tablero(listaFb)

#Corrobora que los disparos si los disparso que acerto son iguales a los barcos, si si significa que gano 
if disparos_acertados == nBarcos:
      print("\n¡Felicidades Jugador 1! ¡Hundiste todos los barcos!")

elif disparos_fallados == nDisparos or disparos_acertados+ disparos_fallados > nDisparos:
    print("\n Has perdido jugador 1 ")



if disparos_acertadosb == nBarcos:
    print("\n¡Felicidades Jugador 2! ¡Hundiste todos los barcos!")

#aca si los disparos fallados son iguales a los disparos(disparo todo mal) y si los disparos acertados mas los fallido son mas que los disparos entonces significa que perdio
elif disparos_falladosb == nDisparos or disparos_acertadosb + disparos_falladosb > nDisparos :
    print("\n Has perdido jugador 2")
