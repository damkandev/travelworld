from utils.limpiarPantalla import clear
from models.userManager import eliminar_usuario, modificar_usuario, asignar_rol
import time

class adminUsers:
    def adminUsers(self):
        clear()
        print("Administrar usuarios")
        print("-----------------")
        print("1. Eliminar usuario")
        print("2. Modificar usuario")
        print("3. Asignar rol")
        print("0. Salir")
        try:
            op = int(input("Seleccione una opción: "))
        except:
            print("Ingrese una opción válida")
            return

        while True:
            if op == 1:
                username = str(input("Ingrese el nombre de usuario a eliminar: "))
                confirmacion = int(input("¿Está seguro que desea eliminar el usuario? (1: Si, 0: No): "))
                if confirmacion == 1:
                    if eliminar_usuario(username):
                        print("Usuario eliminado exitosamente")
                        break
                    else:
                        print("Error al eliminar usuario")
                        break
                else:
                    print("Operación cancelada")
            elif op == 2:
                username = str(input("Ingrese el nombre de usuario a modificar: "))
                rut = str(input("Ingrese el rut: "))
                full_name = str(input("Ingrese el nombre completo: "))
                password = str(input("Ingrese la contraseña: "))
                if modificar_usuario(username, rut, password, full_name):
                    print("Usuario modificado exitosamente")
                else:
                    print("Error al modificar usuario")
            elif op == 3:
                username = str(input("Ingrese el nombre de usuario a asignar rol: "))
                rol = int(input("Ingrese el rol (1: Administrador, 0: Usuario): "))
                try:
                    if asignar_rol(username, rol):
                        print("Rol asignado exitosamente")
                        time.sleep(0.5)
                        break
                    else:
                        print("Error al asignar rol")
                        time.sleep(0.5)
                        break
                except:
                    print("Ingrese una opción válida")
                    break
            elif op == 0:
                return