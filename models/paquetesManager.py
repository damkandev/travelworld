from database import conexion
from .models import Paquete
import json

# Los destinos seran enviados en un dict, por que el atributo en la DB es JSON
def crear_paquete(nombre, destinos, precio_total):
    try:
        cursor = conexion.cursor()
        # Convertir destinos a JSON
        destinos_json = json.dumps(destinos)
        
        # Inserta el paquete
        query_paquete = "INSERT INTO paquete_turistico (nombre, destinos, precio_total) VALUES (%s, %s, %s)"
        cursor.execute(query_paquete, (nombre, destinos_json, precio_total))
        paquete_id = cursor.lastrowid

        # Inserta los destinos en la tabla intermedia
        query_destino = "INSERT INTO paquete_destino (paquete_id, destino_id, fecha_inicio, fecha_fin, precio_unico) VALUES (%s, %s, %s, %s, %s)"
        for destino in destinos:
            params_destino = (
                paquete_id,
                destino['destino_id'],
                destino['fecha_inicio'],
                destino['fecha_termino'],
                destino['precio_unico']
            )
            cursor.execute(query_destino, params_destino)

        conexion.commit()
        return True
    except Exception as e:
        conexion.rollback()
        print(f"Error al crear paquete: {e}")
        return e
    finally:
        cursor.close()

def mostrar_paquete(identificador):
    try:
        cursor = conexion.cursor()
        # Obtén la información del paquete
        query_paquete = "SELECT * FROM paquete_turistico WHERE id = %s"
        cursor.execute(query_paquete, (identificador,))
        paquete = cursor.fetchone()

        if not paquete:
            return None

        # Consulta los destinos asociados al paquete
        query_destinos = """
        SELECT d.id, d.nombre, pd.fecha_inicio, pd.fecha_fin, pd.precio_unico
        FROM paquete_destino pd
        JOIN destino d ON pd.destino_id = d.id
        WHERE pd.paquete_id = %s
        """
        cursor.execute(query_destinos, (identificador,))
        destinos = cursor.fetchall()

        paquete_object = Paquete(
            identificador=paquete[0],
            nombre=paquete[1],
            destinos=[{
                'destino_id': destino[0],
                'nombre_destino': destino[1],
                'fecha_inicio': destino[2],
                'fecha_fin': destino[3],
                'precio_unico': destino[4],
            } for destino in destinos],
            precio_total=paquete[2]
        )

        return paquete_object
    except Exception as e:
        print(f"Error al mostrar paquete: {e}")
        return None
    finally:
        cursor.close()

def modificar_paquete(identificador, nombre, destinos, precio_total):
    try:
        cursor = conexion.cursor()
        # Actualizar el paquete
        query_paquete = "UPDATE paquete_turistico SET nombre = %s, precio_total = %s WHERE id = %s"
        cursor.execute(query_paquete, (nombre, precio_total, identificador))

        # Eliminar los destinos antiguos del paquete
        query_delete_destinos = "DELETE FROM paquete_destino WHERE paquete_id = %s"
        cursor.execute(query_delete_destinos, (identificador,))

        # Insertar los nuevos destinos
        query_insert_destino = "INSERT INTO paquete_destino (paquete_id, destino_id, fecha_inicio, fecha_fin, precio_unico) VALUES (%s, %s, %s, %s, %s)"
        for destino in destinos:
            params_destino = (
                identificador,
                destino['destino_id'],
                destino['fecha_inicio'],
                destino['fecha_fin'],
                destino['precio_unico']
            )
            cursor.execute(query_insert_destino, params_destino)

        conexion.commit()
        print("Modificación exitosa")
        return True
    except Exception as e:
        conexion.rollback()
        print(f"Error al modificar paquete: {e}")
        return e
    finally:
        cursor.close()


def eliminar_paquete(identificador):
    try:
        cursor = conexion.cursor()
        # Eliminar los destinos relacionados
        query_delete_destinos = "DELETE FROM paquete_destino WHERE paquete_id = %s"
        cursor.execute(query_delete_destinos, (identificador,))

        # Eliminar el paquete
        query_delete_paquete = "DELETE FROM paquete_turistico WHERE id = %s"
        cursor.execute(query_delete_paquete, (identificador,))

        conexion.commit()
        print("Eliminación exitosa")
        return True
    except Exception as e:
        conexion.rollback()
        print(f"Error al eliminar paquete: {e}")
        return e
    finally:
        cursor.close()


def listar_paquetes():
    try:
        cursor = conexion.cursor()
        # Consulta los paquetes
        query_paquetes = "SELECT * FROM paquete_turistico"
        cursor.execute(query_paquetes)
        paquetes = cursor.fetchall()

        paquetes_list = []
        for paquete in paquetes:
            paquete_id = paquete[0]

            # Consulta los destinos asociados al paquete
            query_destinos = """
            SELECT d.id, d.nombre, pd.fecha_inicio, pd.fecha_fin, pd.precio_unico
            FROM paquete_destino pd
            JOIN destino d ON pd.destino_id = d.id
            WHERE pd.paquete_id = %s
            """
            cursor.execute(query_destinos, (paquete_id,))
            destinos = cursor.fetchall()

            paquetes_list.append(Paquete(
                identificador=paquete[0],
                nombre=paquete[1],
                destinos=[{
                    'destino_id': destino[0],
                    'nombre_destino': destino[1],
                    'fecha_inicio': destino[2],
                    'fecha_fin': destino[3],
                    'precio_unico': destino[4],
                } for destino in destinos],
                precio_total=paquete[2]
            ))

        return paquetes_list
    except Exception as e:
        print(f"Error al listar paquetes: {e}")
        return []
    finally:
        cursor.close()