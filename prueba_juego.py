#PIEDRA PAPEL O TIJERA
#El juego consiste en que la computadora y el jugador toamran una de las tres opciones. y el
#programa determinará quien de los dos ganó, o quien perdió o en el último de los casos si hubo empate.
#el jugador podra jugar las veces que desee o bien hasta que lo finalice.

import random
import time
from time import sleep
def eleccion_computadora():
    numero_random=random.randint(0,2)
    opciones=["PIEDRA", "PAPEL", "TIJERAS"]
    x= opciones[numero_random]
    return x

def obtenerResultados(eleccion_pc, eleccion_jugador):
    if(eleccion_pc==eleccion_jugador):
        print("\t\t\t :-v EMPATE :-v")
    elif(eleccion_pc=="PIEDRA" and eleccion_jugador=="TIJERAS"):
        print("\t\t\t :-( PERDISTE :-(")
    elif(eleccion_pc=="PAPEL" and eleccion_jugador=="PIEDRA"):
        print("\t\t\t :-( PERDISTE :-(")
    elif(eleccion_pc=="TIJERA" and eleccion_jugador=="PAPEL"):
        print("\t\t\t :-( PERDISTE :-(")
    elif(eleccion_pc=="PIEDRA" and eleccion_jugador=="PAPEL"):
        print("\t\t\t :-D GANASTE :-D")
    elif(eleccion_pc=="PAPEL" and eleccion_jugador=="TIJERAS"):
        print("\t\t\t :-D GANASTE :-D")
    elif(eleccion_pc=="TIJERAS" and eleccion_jugador=="PIEDRA"):
        print("\t\t\t :-D GANASTE :-D")

        

print("\t\t\tJUEGO PIEDRA PAPEL O TIJERAS\n Intenta ganar las veces que quieras!!")
x="s"
while x!="n" and x!="N":
    print("Elija una opcion\nPiedra \nPapel \nTijeras")
    eleccion_jugador=input("\tElija una opción->").upper()
    if(eleccion_jugador!="PIEDRA" and eleccion_jugador!="PAPEL" and eleccion_jugador!="TIJERAS"):
        print("\tEsta opcion no existe, vuelva a intentar.")
    else:
        print('\t\tTu eleccion fue: \t', eleccion_jugador)
        sleep(0.9)
        eleccion_pc=eleccion_computadora()
        print("\t\tLa computadora elegió: \t", eleccion_pc)
        sleep(0.9)
        obtenerResultados(eleccion_pc,eleccion_jugador)
    x=input("Quieres continuar \ns/n\n->")

print("\t\t\t !!!Gracias por jugar¡¡¡")
K=input()
