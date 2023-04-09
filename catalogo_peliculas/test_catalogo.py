# from dominio.Pelicula import Pelicula
# from servicio.catalogo_Pelicula import CatalogoPeliculas as cp
#
# opcion = None
# while opcion != 4:
#     try:
#         print(f"Opciones:")
#         print(f"1 Agregar pelicula:")
#         print(f"2 Listar pelicula:")
#         print(f"3 Eliminar catalogo:")
#         print(f"4 Salir:")
#         opcion = int(input("Escribie tu opcion 1/4:"))
#         if opcion == 1:
#             nombrePelicula = (input("Proporcione una pelicula:"))
#             Pelicula = nombrePelicula
#             cp.agregar_pelicula(Pelicula)
#         elif opcion == 2:
#             cp.listar_peliculas()
#         elif opcion == 3:
#             cp.eliminar_pelicula()
#     except Exception as e:
#         print("Error".center(50,"-"))
#         opcion = None
# else:
#     print("Fin")
from dominio.Pelicula import Pelicula
from servicio.catalogo_Pelicula import CatalogoPeliculas as cp

opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Película')
        print('2. Listar Películas')
        print('3. Eliminar catálogo películas')
        print('4. Salir')
        opcion = int(input('Escribe tu opción (1-4): '))
        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la película: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrió un error {e}')
        opcion = None
else:
    print('Salimos del programa...')


