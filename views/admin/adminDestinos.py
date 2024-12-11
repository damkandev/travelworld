from utils.limpiarPantalla import clear
from models.destinosManager import  agregar_destino, mostrar_destino, modificar_destino, listar_destinos, eliminar_destino
from tabulate import tabulate

class adminDestino:
    def adminDestino(self):
        clear()
        while True:
            print("Administrar Destinos")
            print("-----------------")
            print("1. Listar destinos")
            print("2. Agregar destino")
            print("3. Mostrar destino")
            print("4. Modificar destino")
            print("5. Eliminar destino")
            print("0. Salir")
            try:
                op = int(input("Seleccione una opción: "))
            except:
                print("Ingrese una opción válida")
                return
            if op == 1:
                clear()
                destinos = listar_destinos()
                destinos_data = [[destino.identificador, destino.nombre, destino.descripcion, destino.actividades] for destino in destinos]
                headers = ["ID", "Nombre", "Descripción"]
                print(tabulate(destinos_data, headers, tablefmt="grid"))
                input("Presione una tecla para continuar...")
            elif op == 2:
                clear()
                nombre = str(input("Ingrese el nombre del destino: "))
                descripcion = str(input("Ingrese la descripción del destino: "))
                actividades = str(input("Ingrese las actividades del destino: "))
                precio = int(input("Ingrese el precio del destino: "))
                if agregar_destino(nombre, descripcion, actividades, precio):
                    print("Destino agregado exitosamente")
                else:
                    print("Error al agregar destino")
            elif op == 3:
                clear()
                nombre = str(input("Ingrese el nombre del destino: "))
                destino = mostrar_destino(nombre)
                destino_data = [[destino.identificador, destino.nombre, destino.descripcion, destino.actividades, destino.precio]] if destino else []
                headers = ["Id", "Nombre", "Descripción", "Actividades", "Precio"]
                if destino:
                    print(tabulate(destino_data, headers, tablefmt="grid"))
                    input("Presione una tecla para continuar...")
                else:
                    print("Error al mostrar destino")
            elif op == 4:
                clear()
                nombre = str(input("Ingrese el nombre del destino a modificar: "))
                destino = mostrar_destino(nombre)
                if destino:
                    descripcion = str(input("Ingrese la descripción del destino: "))
                    actividades = str(input("Ingrese las actividades del destino: "))
                    precio = int(input("Ingrese el precio del destino: "))
                    if modificar_destino(destino.identificador, nombre, descripcion, actividades, precio):
                        print("Destino modificado exitosamente")
                    else:
                        print("Error al modificar destino")
                else:
                    print("Destino no encontrado")
            elif op == 5:
                clear()
                nombre = str(input("Ingrese el nombre del destino a eliminar: "))
                confirmacion = int(input("¿Está seguro que desea eliminar el destino? (1: Si, 0: No): "))
                if confirmacion == 1:
                    if eliminar_destino(nombre):
                        print("Destino eliminado exitosamente")
                        break
                    else:
                        print("Error al eliminar destino")
                        break
                else:
                    print("Operación cancelada")
            elif op == 0:
                return