Juego Piedra, Papelo Tijera

Este poryecto consiste en que el computador y jugador podran elejir una de las tres opciones, el jugador podra escoger la opcion que mas le agrade, el computador podra elegir de manera aleatoria, de tal manera que el jugador pueda jugar las veces que el desee o hasta que el lo quiera finalizar.
importamos la libreria random
importamos la libreria time, que se utiliza para manejar el tiempo en el programa.
importa la función sleep de la libreria time, que se utiliza para hacer una pausa en el programa.
definimos las una función llamada eleccion_computadora que generará una elección aleatoria para la computadora.
generamos un número aleatorio entre 0 y 2 y lo asigna a la variable numero_random.
creamos una lista llamada opciones con las opciones posibles para el computador.
asigne el valor de la opción seleccionada aleatoriamente a la variable x.
en el return devuelve el valor de x.
define una función llamada obtenerResultados que compara la elección de la computadora y del jugador para determinar el resultado del juego.
verifica si la elección de la computadora es igual a la elección del jugador e imprime un mensaje de empate si es el caso. 
en los casos contrarios en utilice el elif donde definimos los casos donde puede perder o puede ganar 
utilice un bucle while donde defini mientras x no sea igual a "n" y no sea igual a "N", se ejecuta el siguiente bloque de código.
upper(): solicita al jugador que ingrese una opción y lo convierte a mayúsculas.
en la funcion sleep(0.9): hace una pausa de 0.9 segundos.
x=input("Quieres continuar \ns/n\n->"): solicita al jugador si desea continuar jugando.
en el ultimo print muestra un mensaje de agradecimiento por jugar.
 K=input(): espera a que el usuario presione cualquier tecla.