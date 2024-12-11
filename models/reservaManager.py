from database import conexion
from .models import Paquete
from utils.userSession import UserSession

def listar_reservas():
    try:
        cursor = conexion.cursor()
        # Obtener el nombre de usuario actual
        username = UserSession.get_current_user()
        if not username:
            raise Exception("No hay usuario autenticado")

        # Consulta las reservas del usuario actual
        query_reservas = "SELECT * FROM reserva WHERE username = %s"
        cursor.execute(query_reservas, (username,))
        reservas = cursor.fetchall()

        reservas_list = []
        for reserva in reservas:
            reservas_list.append({
                'identificador': reserva[0],
                'id_paquete': reserva[1],
                'id_usuario': reserva[2]
            })

        return reservas_list
    except Exception as e:
        print(f"Error al listar reservas: {e}")
        return []
    finally:
        cursor.close()

def eliminar_reserva(identificador):
    try:
        cursor = conexion.cursor()
        # Eliminar la reserva
        query_delete_reserva = "DELETE FROM reserva WHERE id = %s"
        cursor.execute(query_delete_reserva, (identificador,))

        conexion.commit()
        print("Eliminación exitosa")
        return True
    except Exception as e:
        conexion.rollback()
        print(f"Error al eliminar reserva: {e}")
        return e
    finally:
        cursor.close()

def crear_reserva(username, paquete_id):
    try:
        cursor = conexion.cursor()
        query = "INSERT INTO reserva (username, paquete_id) VALUES (%s, %s)"
        cursor.execute(query, (username, paquete_id))
        conexion.commit()
        return True
    except Exception as e:
        conexion.rollback()
        print(f"Error al crear reserva: {e}")
        return False
    finally:
        cursor.close()