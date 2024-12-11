from views.mainView import Menu
from database import conexion
from utils.limpiarPantalla import clear
from models.Auth import autenticar

if conexion:
  clear()
  
  menu = Menu()
  menu.mostrarMenu()