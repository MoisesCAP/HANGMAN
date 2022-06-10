
import os
import random
import time

contador = 0
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

# Base del juego
def interface(data_list,contador):
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
            assert user_word.islower(), "Ingresa una letra valida..."
            
            if user_word in list_words or user_word in wrong_words:
                print('Ya ingresaste esa letra, prueba con otra...')
                time.sleep(1.5)
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
                    time.sleep(1)
                    break

        if  VIDAS == 0:
            os.system('clear')
            print(hangman_pictures[6])
            print(f'PERDISTE! VIDAS = {VIDAS}')
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
                print(hangman_pictures[contador])
                print(f'VIDAS = {VIDAS}')
                print()
                print(status)

            else: 
                print()
                print(f'GANASTE! la palabra era "{secret_word}"')
                print()
                break

# Funcion que guarda el contenido de "data_ahorcado" en una lista 
def run():

    print()
    print('BIENVENIDO AL JUEGO DEL AHORCADO')

    with open('./data_ahorcado.txt', 'r', encoding='utf-8') as f:
        data_list = [i for i in f] # list comprehension

    # Para imprimir la imagen correspondiente 
    print(hangman_pictures[contador])
    print()

    interface(data_list,contador) 


if __name__ == '__main__':
    run()