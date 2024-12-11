from werkzeug.security import generate_password_hash, check_password_hash

def generar_hash_clave(clave):
    return generate_password_hash(clave)

clave = "hola"
hash_clave = generar_hash_clave(clave)
print("Hash de la clave:", hash_clave)
print(f"contraseña:{hash_clave}")
print("Verificando la clave:", check_password_hash("scrypt:32768:8:1$gS1FdVlb4kKXooTz$1580c6311a58eab02ca5e3ab0de63b0825d20feebe9d6de4ba7178b95253a2b992126b28c6e1209c1abe5785d835104663dd452bcaa6b8549661351f02b6eca8", clave))