from utils.limpiarPantalla import clear
from models.paquetesManager import listar_paquetes
from models.reservaManager import crear_reserva
from utils.userSession import UserSession
from tabulate import tabulate

class UserPaquetes:
    @staticmethod
    def reservar_paquete():
        clear()
        username = UserSession.get_current_user()
        if not username:
            print("No hay usuario autenticado.")
            return

        # Listar paquetes disponibles
        paquetes_disponibles = listar_paquetes()
        if not paquetes_disponibles:
            print("No hay paquetes disponibles para reservar.")
            input("Presione una tecla para continuar...")
            return

        print("Paquetes disponibles:")
        paquetes_data = [[paquete.identificador, paquete.nombre, paquete.precio_total] for paquete in paquetes_disponibles]
        headers = ["ID", "Nombre", "Precio Total"]
        print(tabulate(paquetes_data, headers, tablefmt="grid"))

        paquete_id = input("Ingrese el ID del paquete que desea reservar: ")
        paquete = next((p for p in paquetes_disponibles if str(p.identificador) == paquete_id), None)
        if not paquete:
            print("ID de paquete no válido. Intente nuevamente.")
            return

        if crear_reserva(username, paquete.identificador):
            print("Reserva realizada exitosamente.")
        else:
            print("Error al realizar la reserva.")
        input("Presione una tecla para continuar...")

