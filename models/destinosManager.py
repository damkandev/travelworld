from database import conexion
from .models import Destino

def agregar_destino(nombre, descripcion, actividades, precio):
    try:
        cursor = conexion.cursor()
        query = "INSERT INTO destino (nombre, descripcion, actividades, precio) VALUES (%s, %s, %s, %s)"
        params = (nombre, descripcion, actividades, precio)
        cursor.execute(query, params)
        conexion.commit()
        return True
    except Exception as e:
        return e
    finally:
        cursor.close()

def mostrar_destino(nombre):
    try:
        cursor = conexion.cursor()
        query = "SELECT * FROM destino WHERE nombre = %s"
        params = (nombre,)
        cursor.execute(query, params)
        destino = cursor.fetchone()
        if not destino:
            return None

        destino_object = Destino(
            identificador=destino[0],
            nombre=destino[1],
            descripcion=destino[2],
            actividades=destino[3],
            precio=destino[4]
        )

        return destino_object
    except Exception as e:
        print(f"Error al mostrar destino: {e}")
        return None
    finally:
        cursor.close()

def modificar_destino(idestino, nombre, descripcion, actividades, precio):
    try:
        cursor = conexion.cursor()
        query = "UPDATE destino SET nombre = %s, descripcion = %s, actividades = %s, precio = %s WHERE id = %s"
        params = (nombre, descripcion, actividades, precio, idestino)
        cursor.execute(query, params)
        conexion.commit()
        print("Modificación exitosa")
        return True
    except Exception as e:
        print(f"Error al modificar destino: {e}")
        return e
    finally:
        cursor.close()

def listar_destinos():
  try:
    cursor = conexion.cursor()
    query = "SELECT * FROM destino"
    cursor.execute(query)
    destinos = cursor.fetchall()
    return [Destino(
      identificador=destino[0],
      nombre=destino[1],
      descripcion=destino[2],
      actividades=destino[3],
      precio=destino[4]
    ) for destino in destinos]
  except Exception as e:
    print(f"Error al listar destinos: {e}")
    return []
  finally:
    cursor.close()

def eliminar_destino(nombre):
  try:
    cursor = conexion.cursor()
    query = "DELETE FROM destino WHERE nombre = %s"
    params = (nombre,)
    cursor.execute(query, params)
    conexion.commit()
    return True
  except Exception as e:
    return e
  finally:
    cursor.close()

def ver_destino(nombre):
  try:
    cursor = conexion.cursor()
    query = "SELECT * FROM destino WHERE nombre = %s"
    params = (nombre,)
    cursor.execute(query, params)
    destino = cursor.fetchone()
    return Destino(
      nombre = destino[0],
      descripcion = destino[1],
      actividades = destino[2]
    )
  except Exception as e:
    return e
  finally:
    cursor.close()