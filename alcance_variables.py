print('*** Alcance de variables ***')

#variable global
contador_global = 0

def incrementar_contador():
    #declaramos una variable local
    contador_local = 0
    #usar la variable global
    global contador_global
    contador_global +=1
    #incrementar la variable local
    contador_local += 1
    #imprimimos ambos contadores
    print(f'Contador local: {contador_local}')
    print(f'contador global: {contador_global}')

#llamos varias veces la funcion
incrementar_contador()
incrementar_contador()
incrementar_contador()


#terminando el programa
print(f'valor variable global: {contador_global}')
