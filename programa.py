# Python 3.10
# Repositorio en SSH: git@github.com:MoisesCAP/HANGMAN.git
# Repo. en HTTPS: https://github.com/MoisesCAP/HANGMAN.git

import os
import random

contador = 0 # Para llevar un orden de la imagen que se imprimirá
status = '' # Para mostrar el estado de la adivinanza 
list_words = [] # Para guardar las letras correctas 
wrong_words = [] # Para guardar las letras erróneas
VIDAS = 6 # Máximo de vidas

hangman_pictures = ['''
    +---+
    |   |
        |
        |
        |
        |

    =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']

# Se encarga de mostrar los resultados de cada ejecución de la adivinanza
def conclusion(VIDAS, secret_word, list_words, status):
 
    if  VIDAS == 0:
            os.system('clear')
            print()
            print(hangman_pictures[6])
            print(f'PERDISTE! VIDAS = {VIDAS}')
            print(f'la palabra era "{secret_word}"')
            print()

    else:
        print()
        
        for i in secret_word:
            if i in list_words:
                status += i
            else:
                status += '_ '

        if status != secret_word:
            os.system('clear')
            print(hangman_pictures[contador])
            print(f'VIDAS = {VIDAS}')
            print()
            print(status)
            
            game(secret_word, list_words, wrong_words, VIDAS, contador)

        else: 
            os.system('clear')
            print()
            print(f'GANASTE! la palabra era "{secret_word}"')
            print()      


# Se encarga de establecer la interacción con el usuario
def game(secret_word, list_words, wrong_words, VIDAS, contador):
        
    while True:
        print()
        user_word = input('Ingresa una letra: ')
        print()
        user_word = user_word.lower().replace(' ','')
        print()

        assert user_word.islower(), "EL PROGRAMA SOLO ACEPTA LETRAS."
        assert(len(user_word) == 1), "INGRESA UNA LETRA A LA VEZ"
        
        if user_word in list_words or user_word in wrong_words:
            os.system('clear')
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
                os.system('clear')
                print('Fallaste...')
                break

    conclusion(VIDAS, secret_word, list_words, status)
    

# Guarda el contenido de "data_ahorcado" en una lista y escoge la "secret_word"
def run():

    with open('./data_ahorcado.txt', 'r', encoding='utf-8') as f:
        data_list = [i for i in f] # list comprehension

    # Para imprimir la imagen correspondiente 
    print(hangman_pictures[contador])
    print()

    secret_word = random.choice(data_list).replace('\n','')

    print(f'VIDAS = {VIDAS}')
    print()
    
    print('Palabra a adivinar: ','_ '*len(secret_word))
    print()
    print('='*40)
    print()

    game(secret_word, list_words, wrong_words, VIDAS, contador) 


# INICIO
if __name__ == '__main__':
    print()
    print('BIENVENIDO AL JUEGO DEL AHORCADO')
    run() 
