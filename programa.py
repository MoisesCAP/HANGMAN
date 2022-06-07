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

def run():
    with open('C:/Users/Brunilda/Desktop/PROGRAMMING/data_ahorcado.txt', 'r', encoding='utf-8') as f:
        list_words = []
        for i in f:
            list_words.append(i)
        f.close()

if __name__ == '__main__':
    run()