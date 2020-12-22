# -*- coding: utf-8 -*-

##
# @file ahorcado.py
# @brief Solución para el proyecto de ahorcado del curso de python
# @author AbrahamRH
# @version 1.0
# @date 2020-12-21


import re  # Ignorar esta linea, se usa para validar entradas con expresiones regulares


# -------------------------------
##
# @brief @brief Función principal desde donde iniciara el programa
#
# -------------------------------
def main():
    printMenu()
    dificultad = int(input("->  "))
    while validateEntry(str(dificultad)):
        if dificultad == 1:
            juego({"pez": "Animal marino", "sol": "Estrella",
                   "luz": "Permite ver en la oscuridad"}, 5)
            break
        elif dificultad == 2:
            juego({"comida": "Puede ser un hotdog",
                   "edificio": "Construcción más grande que una casa", "tienda": "Lugar comprar"}, 3)
            break
        elif dificultad == 3:
            juego({"dinosaurio": "Animal prehistorico",
                   "computadora": "Equipo electronico", "laberinto": "Lugar para perderse"}, 2)
            break
        elif dificultad == 0:
            print("\tVuelva pronto!!")
            break
        else:
            print("Opción no valida")

# -------------------------------
##
# @brief Función para inprimir el menu de inicio
#
# -------------------------------


def printMenu():
    print("="*50)
    print("Ahorcado")
    print("="*50)
    print("""
        Elige la dificultad para jugar
        1) Fácil
        2) Intermedio
        3) Difícil

        0) Salir del juego
          """)
    print("="*50)


# -------------------------------
##
# @brief  Función para validar una entrada del usuario
#
# @param entry cadena o número a evaluar
#
# @return True: si es valido, False: caso contrario
#
# NOTE: Esta es una función rápida usando expresiones regulares
#       Se espera que el alumno realíce lo mismo con estructuras
#       de control y no con expresiones regulares
# -------------------------------
def validateEntry(entry):
    regex = "[a-zA-Z]|[0-3]"
    return re.match(regex, entry) and len(entry) == 1


# -------------------------------
##
# @brief Función de inicio del juego
#
# @param diccionario Diccionaro de las palabras que se tienen que buscar con sus pistas
# @param intentosMax El numero de intentos máximos para jugar
#
# -------------------------------
def juego(diccionario, intentosMax):
    palabras = list(diccionario.keys())
    pistas = list(diccionario.values())
    palabraActual = palabras[numPalabra]
    numPalabra = 0
    intentos = 0
    memoria = {}
    while True:
        if intentos != intentosMax + 1:
            cadena = cadenaEspacios(palabras[numPalabra], memoria)
            printGame(intentos, intentosMax, cadena, pistas[numPalabra])
            verification = verificarLetra(memoria, palabras[numPalabra])
            if verification is not False:
                memoria, palabras[numPalabra] = verification
            else:
                intentos += 1
            if len(memoria) == len(palabras[numPalabra]):
                print("="*50)
                print("Lo lograste, sigamos con siguiente palabra : ")
                print("="*50)
                palabraActual = palabras[numPalabra]
                numPalabra += 1
                memoria.clear()
                intentos = 0
        else:
            print(f"""
                  Perdiste :c
        La palabra a encontrar era {palabras[numPalabra]}
                  """)
            break
        if numPalabra == len(palabras):
            print("="*50)
            print("""
            ¡¡¡¡ Felicidades Ganaste !!!!
                  """)
            print("="*50)
            break
    main()


# -------------------------------
##
# @brief Función para verificar si la letra introdujo es correcta
#
# @param memoria Diccionario en la que se almacenara la letra encontrada
# @param palabra Palabra que se esta buscando en el juego
#
# @return Tupla (memoria,palabra): si se encontro la palabra, False: Si no se encontro
# -------------------------------
def verificarLetra(memoria, palabra):
    letra = input("-> ")
    if not validateEntry(letra):
        return False
    if letra in palabra:
        ind = palabra.index(letra)
        palabra = palabra.replace(letra, "$", 1)
        memoria[ind] = letra
        return memoria, palabra
    else:
        return False


# -------------------------------
##
# @brief Función para imprimir la partida actual
#
# @param intentos Número de intento actual del intento
# @param intentosMax Numero sde intentos máximos
# @param cadena Cadena con los elementos que se han encontrado hasta el momento
# @param pista Cadena que contiene la pista del la palabra
#
# -------------------------------
def printGame(intentos, intentosMax, cadena, pista):
    print("="*50)
    print("Ahorcado")
    print("="*50)
    print(f"""
         Intentos: {intentos}/{intentosMax}
         Palabra : {cadena}
         Pista : {pista}
          """)
    print("="*50)


# -------------------------------
##
# @brief Función para pasar buscar los caracteres encontrados y crear la cadena con lineas
#
# @param palabra Cadena que contienen la palabra actual a buscar
# @param memoria Diccionario con los elementos encontrados y su posición
#
# @return Cadena con las lineas y elementos encontrados
# -------------------------------
def cadenaEspacios(palabra, memoria):
    size = len(palabra)
    cadena = ""
    for i in range(size):
        if i in memoria:
            cadena += " " + memoria[i] + " "
        else:
            cadena += " _ "
    return cadena


if __name__ == "__main__":
    main()
