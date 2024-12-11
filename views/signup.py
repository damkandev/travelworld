from yaspin import yaspin, Spinner
from yaspin.spinners import Spinners
from models.userManager import registrarme, get_usuario
from utils.userSession import UserSession
import time

class Signup:
    @staticmethod
    def signup():
        username = input("Ingrese su nombre de usuario: ")
        rut = input("Ingrese su rut: ")
        full_name = input("Ingrese su nombre completo: ")
        password = input("Ingrese su contraseña: ")

        try:
            with yaspin(text="Registrando...", color="yellow") as spinner:
                time.sleep(0.5)
                if get_usuario(username):
                    spinner.text = "El usuario ya existe, inicia sesión"
                    spinner.fail("✖")
                    return False
                if registrarme(username, rut, password, full_name):
                    spinner.ok("✔")
                    print("Usuario registrado exitosamente")
                    UserSession.set_current_user(username)  # Guardar el nombre de usuario
                    return True
                else:
                    spinner.fail("✖")
                    print("Error al registrar usuario")
                    return False
        except Exception as e:
            print(str(e))
            return False