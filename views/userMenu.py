from utils.limpiarPantalla import clear
from models.paquetesManager import listar_paquetes, mostrar_paquete
from views.user.userPaquetes import UserPaquetes
from views.user.userReservas import listar_reservas
from tabulate import tabulate

class UserMenu:
    def UserMenu(self):
        clear()
        while True:
            print("Menú de usuario")
            print("-----------------")
            print("1. Menú reservas")
            print("2. Menú paquetes")
            print("0. Salir")
            try:
                op = int(input("Seleccione una opción: "))
            except:
                print("Ingrese una opción válida")
                return

            if op == 1:  # Menú reservas
                clear()
                reservas = listar_reservas()
                if not reservas:
                    print("No hay reservas disponibles.")
                else:
                    reservas_data = [[reserva['identificador'], reserva['id_paquete'], reserva['id_usuario']] for reserva in reservas]
                    headers = ["ID", "ID Paquete", "ID Usuario"]
                    print(tabulate(reservas_data, headers, tablefmt="grid"))
                input("Presione una tecla para continuar...")
            elif op == 2:  # Menú paquetes
                clear()
                print("Menú de paquetes")
                print("-----------------")
                print("1. Listar paquetes")
                print("2. Reservar paquete")
                print("0. Volver")
                try:
                    sub_op = int(input("Seleccione una opción: "))
                except:
                    print("Ingrese una opción válida")
                    continue

                if sub_op == 1:
                    clear()
                    paquetes = listar_paquetes()
                    if not paquetes:
                        print("No hay paquetes disponibles.")
                    else:
                        paquetes_data = [[paquete.identificador, paquete.nombre, paquete.precio_total] for paquete in paquetes]
                        headers = ["ID", "Nombre", "Precio Total"]
                        print(tabulate(paquetes_data, headers, tablefmt="grid"))
                    input("Presione una tecla para continuar...")
                elif sub_op == 2:
                    UserPaquetes.reservar_paquete()
                elif sub_op == 0:
                    continue
                else:
                    print("Ingrese una opción válida")
            elif op == 0:
                return
            else:
                print("Ingrese una opción válida")