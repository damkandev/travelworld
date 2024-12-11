from werkzeug.security import check_password_hash
from models.userManager import get_usuario

def autenticar(username, password):
  user = get_usuario(username)
  if not user:
    return
  return check_password_hash(user.password, password)


def is_admin(username):
  user = get_usuario(username)
  if not user:
    return
  if user.is_admin == 1:
    return True
  else:
    return False