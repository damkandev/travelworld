from database import conexion
from .models import Usuario
from werkzeug.security import generate_password_hash
def get_usuario(username):
  try:
    cursor = conexion.cursor()
    query = "SELECT * FROM usuarios WHERE username = %s"
    params = (username,)
    cursor.execute(query, params)
    user = cursor.fetchone()
    if not user:
      return

    user_object = Usuario(
      username = user[0],
      rut = user[1],
      full_name = user[2],
      password = user[3],
      is_admin = user[4]
    )

    return user_object
  except Exception as e:
    return e
  finally:
    cursor.close()

def registrarme(username, rut, password, full_name):
  try:
    cursor = conexion.cursor()
    query = "INSERT INTO usuarios (username, rut, full_name, password) VALUES (%s, %s, %s, %s)"
    params = (username, rut, full_name, generate_password_hash(password))
    cursor.execute(query, params)
    conexion.commit()
    return True
  except Exception as e:
    return e
  finally:
    cursor.close()

def modificar_usuario(username, rut, full_name, password):
  try:
    cursor = conexion.cursor()
    query = "UPDATE usuarios SET rut = %s, full_name = %s, password = %s, is_admin = %s WHERE username = %s"
    params = (rut, full_name, generate_password_hash(password), username, 0)
    cursor.execute(query, params)
    conexion.commit()
    return True
  except Exception as e:
    return e
  finally:
    cursor.close()

def eliminar_usuario(username):
  try:
    cursor = conexion.cursor()
    query = "DELETE FROM usuarios WHERE username = %s"
    params = (username,)
    cursor.execute(query, params)
    conexion.commit()
    return True
  except Exception as e:
    return e
  finally:
    cursor.close()

def asignar_rol(username, rol):
  try:
    cursor = conexion.cursor()
    query = "UPDATE usuarios SET is_admin = %s WHERE username = %s"
    params = (rol, username)
    cursor.execute(query, params)
    conexion.commit()
    return True
  except Exception as e:
    return e
  finally:
    cursor.close()