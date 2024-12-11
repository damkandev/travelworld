from models.Auth import autenticar, is_admin
from yaspin import yaspin, Spinner
import time
from utils.limpiarPantalla import clear
from utils.userSession import UserSession

class Login:
    @staticmethod
    def login():
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        with yaspin(text="Autenticando...", color="yellow") as spinner:
            time.sleep(0.5)
            if autenticar(username, password):
                UserSession.set_current_user(username)  # Guardar el nombre de usuario
                clear()
                spinner.text = "Bienvenido " + username + " | Administrador: " + ("Si" if is_admin(username) else "No")
                spinner.ok("✔")
                time.sleep(0.2)
                return [True, is_admin(username)]
            else:
                spinner.text = "Autenticación fallida"
                spinner.fail("✖")
                time.sleep(0.5)
                return [False, False]