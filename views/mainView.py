from utils.limpiarPantalla import clear
from views import login, signup, adminMenu, userMenu
from utils.userSession import UserSession

class Menu:
    def mostrarMenu(self):
        while True:
            clear()
            print("Bienvenid@ a ViajeAventura")
            print("1. Iniciar sesión")
            print("2. Registrarse")
            op = int(input("Seleccione una opción: "))
            if op == 1:
                clear()
                login_result = login.Login.login()
                if not login_result[0]:
                    continue 
                if login_result[1]:
                    admin_menu = adminMenu.adminMenu()
                    admin_menu.adminMenu()
                else:
                    user_menu = userMenu.UserMenu()
                    user_menu.UserMenu()
            elif op == 2:
                clear()
                if signup.Signup.signup():
                    username = UserSession.get_current_user()
                    if username:
                        if login.is_admin(username):
                            admin_menu = adminMenu.adminMenu()
                            admin_menu.adminMenu()
                        else:
                            user_menu = userMenu.UserMenu()
                            user_menu.UserMenu()
                    else:
                        continue  