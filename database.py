from mysql.connector import connect
from colorama import Fore, init
from yaspin import yaspin, Spinner
from yaspin.spinners import Spinners
import os 
import time
init()

def conectar():
  with yaspin(Spinners.arc, text="Estableciendo conexión con el sistema...", color="green") as spinner:
    time.sleep(1)
    try:
        con = connect(
          host="localhost",
          user="root",
          password="",
          database="travelworld",
          port=3306,
        )
        spinner.color = "green"
        spinner.ok("✔")
        return con
    except Exception as e:
        spinner.color = "red"
        spinner.text = "Error al conectar con la base de datos"
        spinner.fail("✘")
        print(e)
        return None

conexion = conectar()