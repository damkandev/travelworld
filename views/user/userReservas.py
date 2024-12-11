from utils.limpiarPantalla import clear
from models.reservaManager import listar_reservas, eliminar_reserva
from tabulate import tabulate
class userReservas:
    def userReservas(self):
      clear()
      print("Menú de reservas")
      print("-----------------")
      print("1. Listar reservas")
      print("2. Eliminar reserva")
      print("0. Salir")
      try:
        op = int(input("Seleccione una opción: "))
      except:
        print("Ingrese una opción válida")
        return

      while True:
        if op == 1:
          clear()
          reservas = listar_reservas()
          reservas_data = [[
              reserva.identificador,
              reserva.id_paquete,
              reserva.id_usuario
          ] for reserva in reservas]
          headers = ["ID", "ID Paquete", "ID Usuario"]
          print(tabulate(reservas_data, headers, tablefmt="grid"))
          input("Presione una tecla para continuar...")
        elif op == 2:
          clear()
          identificador = input("Ingrese el ID de la reserva a eliminar: ")
          if not identificador:
              print("Ingrese un ID válido")
              return
          if eliminar_reserva(identificador):
              print("Reserva eliminada con éxito")
          else:
              print("Error al eliminar la reserva")
          input("Presione una tecla para continuar...")
        elif op == 0:
          return
        else:
          print("Ingrese una opción válida")
          return
