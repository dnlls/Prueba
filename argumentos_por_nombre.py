print('*** Funcion con argumentos por nombre  ***')

def imprimir_persona(nombre, apellido='', edad=0):
    print(f'persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')


#primero llamamos la funcion pasando los argumentos de manera posicional
imprimir_persona('Ricardo', 'Quintana', 32)
#llamar la funcion usando argumentos por nombre
imprimir_persona(nombre='Carlos', apellido= 'Rojas', edad =28)

#llamar la funcion usando argumentos por nombre, pero intercambiando el orden
imprimir_persona(edad=28, apellido='rojas', nombre='carlos')

#argumentos con valor por default
imprimir_persona(nombre='carlos')
imprimir_persona(nombre='carlos', apellido='Rojas')
imprimir_persona(apellido='Rojas',nombre='carlos')