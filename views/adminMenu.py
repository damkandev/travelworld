from utils.limpiarPantalla import clear
from views.admin.adminUsers import adminUsers
from views.admin.adminDestinos import adminDestino
from views.admin.adminPaquetes import adminPaquetes

class adminMenu:
    def adminMenu(self):
        while True:
            clear()
            print("Menú")
            print("-----------------")
            print("1. Menú Administrador")
            print("2. Menú Usuario")
            print("0. Salir")

            op1 = int(input("Seleccione una opción: "))
            if op1 == 1:
                clear()
                print("Bienvenido al menú de administrador")
                print("1. Administrar usuarios")
                print("2. Administrar destinos")
                print("3. Administrar paquetes turisticos")
                print("0. Salir")
                op2 = int(input("Seleccione una opción: "))
                if op2 == 1:
                    admin_users = adminUsers()
                    if admin_users.adminUsers() is None:
                        continue
                elif op2 == 2:
                    admin_destinos = adminDestino()
                    if admin_destinos.adminDestino() is None:
                        continue
                elif op2 == 3:
                    admin_paquetes = adminPaquetes()
                    if admin_paquetes.adminPaquetes() is None:
                        continue
                elif op2 == 0:
                    break
            elif op1 == 2:
                print("Menú Usuario")
            elif op1 == 0:
                break