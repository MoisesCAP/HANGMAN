#---------------REGLAS-----------------
# Debes usar los conceptos vistos en el curso, como por ejemplo: list y dict comprehension,
# manejo de errores (assert, try y except, rais) y manejo de archivos (data.txt)
# aplica os.sys('clear') para limpiar la pantalla despues que el usuario ingresa una letra,
#  esto en forma de bucle

#---------------AYUDAS-----------------
# investiga sobre la funcion 'enumerate'
# el metodo 'get' para los diccionarios puede servir

#---------------MEJORAS----------------
# Implementa codigo ASCII para dibujar 
# Añade un sistema de puntos cada ves que el usuario adivine una palabra
# Haz una interfaz lo mas amigable posible 

import os
import random


def interface(data_list, hangman_pictures, contador):
    list_words = [] 
    wrong_words = []

    VIDAS = 6
    print(f'VIDAS = {VIDAS}')
    print()

    secret_word = random.choice(data_list).replace('\n','')

    print('Palabra a adivinar: ','_ '*len(secret_word))
    print()
    print('='*40)
    print()
    while True:
        
        while True:
            print()
            user_word = input('Ingresa una letra: ').lower().replace(' ','')
            print()
            if user_word in list_words or user_word in wrong_words:
                print('Ya ingresaste esa letra, prueba con otra...')
                print()
                break

            if user_word in secret_word:
                list_words.append(user_word)
                break

            else:
                contador += 1
                VIDAS -= 1
                wrong_words.append(user_word)
                if VIDAS == 0:
                    break
                else:
                    print('Fallaste...')
                    break

        if  VIDAS == 0:
            break
        else:
            os.system('clear')
            print()
            status = ''

            for i in secret_word:
                if i in list_words:
                    status += i
                else:
                    status += '_ '

            if status != secret_word:
                # print(hangman_pictures[contador])
                print(f'VIDAS = {VIDAS}')
                print()
                print(status)

            else: 
                print(f'GANASTE! la palabra era "{secret_word}"')
                break

    os.system('clear')
    # print(hangman_pictures[6])
    print(f'PERDISTE! VIDAS = {VIDAS}')

def run(contador):

    print()
    print('BIENVENIDO AL JUEGO DEL AHORCADO')

    with open('./data_ahorcado.txt', 'r', encoding='utf-8') as f:
        data_list = []
        for i in f:
            data_list.append(i)
    with open('./hangman_pictures.txt', 'r', encoding='utf-8') as m:
        hangman_pictures = []
        for i in m:
            hangman_pictures.append(i)

    # print(hangman_pictures[contador])
    print()

    interface(data_list, hangman_pictures, contador)


if __name__ == '__main__':
    contador = 0
    run(contador)