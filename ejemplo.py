from subprocess import run

if __name__== '__main__':
    run('cls', shell=True)

    listaDePropiedades = ['Nombre', 'Paterno', 'Materno', 'Boleta', 'Semestre', 'Promedio', 'Carrera']
    alumno = {}

    # Se muestra el alumno como un diccionario vacio
    print('alumno', type(alumno) )
    print( alumno )
    print()

    # Se genera un diccionario con la lista de propiedades como claves, y los valores ingresados por el usuario
    for clave in listaDePropiedades:
        valor = input(f'Ingresa tu {clave} ')
        alumno.update( {clave : valor} )
    print()

    # Se muestra la lista de propiedades
    print('listaDePropiedades', type(listaDePropiedades) )
    print( listaDePropiedades )
    print()

    # Se muestra el alumno como un diccionario
    print('alumno', type(alumno) )
    print( alumno )
    print()

    # Se muestra cada pareja clave:valor (items) del diccionario 
    print('alumno.items()', type(alumno.items()) )
    for pareja in alumno.items():
        print( f'{pareja[0]} : {pareja[1]}' )
    print()

    # Se guardan los datos (values) del alumno (diccionario) en un archivo
    ArchivoEscritura = open('agenda.txt', 'w')

    # Para cada pareja del diccionario se guarda el valor [1]
    for pareja in alumno.items():
        ArchivoEscritura.write( pareja[1] )
        
        if pareja[0] != 'Carrera': # Si la clave (pareja[0]) no es la ultima ('Carrera'), se escribe una coma
            ArchivoEscritura.write( ',' )
        
        else: # si no, se escribe un salto de linea
            ArchivoEscritura.write( '\n' )


    ArchivoEscritura.close()

    # Si los datos de UN alumno estan guardados en agenda.txt, 
    # se genera un diccionario en el que se cargaran
    diccionario = {}

    # Se muestra el diccionario vacio
    print('diccionario', type(diccionario) )
    print( diccionario )
    print()
    
    # Se cargan los datos de UN alumno, desde el archivo donde se encuentran
    ArchivoLectura = open('agenda.txt', 'r')

    # Se carga una línea y se le quita el salto de linea con strip('\n')
    linea = ArchivoLectura.readline()
    cadenaSinSalto = linea.strip('\n')

    # Se parte la cadena en una lista de cadenas que estan unidas/separadas por coma
    listaDeCadenas = cadenaSinSalto.split(',')

    # Como la cantidad de cadenas en la lista corresponde a la cantidad de propiedades en la lista de propiedades
    # se genera el diccionario con la misma posicion en cada lista
    n = len(listaDePropiedades)
    for posicion in range(n):
        diccionario.update( { listaDePropiedades[posicion] : listaDeCadenas[posicion]} )

    # Se muestra el diccionario generado con las propiedades deseadas y los datos cargados
    print('diccionario', type(diccionario) )
    print( diccionario )
    print()
    
    # Se muestra cada pareja clave:valor (items) del diccionario 
    print('diccionario.items()', type(diccionario.items()) )
    for pareja in diccionario.items():
        print( f'{pareja[0]} : {pareja[1]}' )
    print()

    # Se cierra el archivo, cuando ya no se necesita
    ArchivoLectura.close()
