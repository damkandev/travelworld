from utils.limpiarPantalla import clear
from models.paquetesManager import listar_paquetes, mostrar_paquete, crear_paquete, modificar_paquete, eliminar_paquete
from models.destinosManager import listar_destinos
from tabulate import tabulate

class adminPaquetes:
    def adminPaquetes(self):
        clear()
        while True:
            print("Administrar Paquetes")
            print("-----------------")
            print("1. Listar paquetes")
            print("2. Crear paquete")
            print("3. Mostrar paquete")
            print("4. Modificar paquete")
            print("5. Eliminar paquete")
            print("0. Salir")
            try:
                op = int(input("Seleccione una opción: "))
            except:
                print("Ingrese una opción válida")
                return
            
            if op == 1:  # Listar paquetes
                clear()
                paquetes = listar_paquetes()
                paquetes_data = [[
                    paquete.identificador, 
                    paquete.nombre, 
                    str(paquete.destinos),  # Asegurar que se vea legible en el terminal
                    paquete.precio_total
                ] for paquete in paquetes]
                headers = ["ID", "Nombre", "Destinos", "Precio total"]
                print(tabulate(paquetes_data, headers, tablefmt="grid"))
                input("Presione una tecla para continuar...")

            elif op == 2:  # Crear paquete
                clear()
                nombre_paquete = input("Ingrese el nombre del paquete: ")
                destinos = []

                # Listar destinos disponibles
                destinos_disponibles = listar_destinos()
                if not destinos_disponibles:
                    print("No hay destinos disponibles para agregar al paquete.")
                    input("Presione una tecla para continuar...")
                    continue
                
                print("Destinos disponibles:")
                destinos_data = [[destino.identificador, destino.nombre, destino.descripcion, destino.actividades, destino.precio] for destino in destinos_disponibles]
                headers = ["ID", "Nombre", "Descripción", "Actividades", "Precio"]
                print(tabulate(destinos_data, headers, tablefmt="grid"))

                while True:
                    destino_id = input("Ingrese el ID del destino (o 'fin' para terminar): ")
                    if destino_id.lower() == 'fin':
                        break
                    destino = next((d for d in destinos_disponibles if str(d.identificador) == destino_id), None)
                    if destino:
                        fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                        fecha_termino = input("Ingrese la fecha de término (YYYY-MM-DD): ")
                        precio = int(input("Ingrese el precio del destino: "))
                        destinos.append({
                            "destino_id": destino.identificador,
                            "nombre_destino": destino.nombre,
                            "fecha_inicio": fecha_inicio,
                            "fecha_termino": fecha_termino,
                            "precio_unico": precio
                        })
                    else:
                        print("ID de destino no válido. Intente nuevamente.")

                if crear_paquete(nombre_paquete, destinos, sum(d["precio_unico"] for d in destinos)):
                    print("Paquete agregado exitosamente")
                else:
                    print("Error al agregar paquete")
                input("Presione una tecla para continuar...")

            elif op == 3:  # Mostrar paquete
                clear()
                identificador = int(input("Ingrese el ID del paquete: "))
                paquete = mostrar_paquete(identificador)
                if paquete:
                    paquete_data = [[
                        paquete.identificador, 
                        paquete.nombre, 
                        str(paquete.destinos), 
                        paquete.precio_total
                    ]]
                    headers = ["ID", "Nombre", "Destinos", "Precio total"]
                    print(tabulate(paquete_data, headers, tablefmt="grid"))
                else:
                    print("No se encontró el paquete.")
                input("Presione una tecla para continuar...")

            elif op == 4:  # Modificar paquete
                clear()
                identificador = int(input("Ingrese el ID del paquete a modificar: "))
                paquete = mostrar_paquete(identificador)
                if paquete:
                    print(f"Datos actuales: Nombre={paquete.nombre}, Destinos={paquete.destinos}, Precio total={paquete.precio_total}")
                    nombre = input("Ingrese el nuevo nombre del paquete: ")
                    destinos = {}
                    while True:
                        nombre_destino = input("Ingrese el nombre del destino (o 'fin' para terminar): ")
                        if nombre_destino.lower() == 'fin':
                            break
                        fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                        fecha_termino = input("Ingrese la fecha de término (YYYY-MM-DD): ")
                        precio = int(input("Ingrese el precio del destino: "))
                        destinos[nombre_destino] = {
                            "fecha_inicio": fecha_inicio,
                            "fecha_termino": fecha_termino,
                            "precio": precio
                        }
                    if modificar_paquete(identificador, nombre, destinos, sum(d["precio"] for d in destinos.values())):
                        print("Paquete modificado exitosamente")
                    else:
                        print("Error al modificar paquete")
                else:
                    print("No se encontró el paquete.")
                input("Presione una tecla para continuar...")

            elif op == 5:  # Eliminar paquete
                clear()
                identificador = int(input("Ingrese el ID del paquete a eliminar: "))
                if eliminar_paquete(identificador):
                    print("Paquete eliminado exitosamente")
                else:
                    print("Error al eliminar paquete")
                input("Presione una tecla para continuar...")

            elif op == 0:  # Salir
                break
            else:
                print("Opción no válida, intente nuevamente.")
                input("Presione una tecla para continuar...")
