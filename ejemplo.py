from subprocess import run

if __name__== '__main__':
    run('cls', shell=True)

    propiedades = ['Nombre', 'Paterno', 'Materno', 'Boleta', 'Semestre', 'Promedio', 'Carrera']
    alumno = {}

    # Se muestra el alumno como un diccionario vacio
    print('alumno', type(alumno) )
    print( alumno )
    print()

    # Se genera un diccionario con la lista de propiedades como claves, y los valores ingresados por el usuario
    for clave in propiedades:
        valor = input(f'Ingresa tu {clave} ')
        alumno.update( {clave : valor} )
    print()

    # Se muestra la lista de propiedades
    print('propiedades', type(propiedades) )
    print( propiedades )
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
