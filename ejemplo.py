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
