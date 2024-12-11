class Usuario:
    def __init__(self, rut, full_name, username, password, is_admin):
        self.username: str = username
        self.rut: str = rut
        self.full_name: str = full_name
        self.password: str = password
        self.is_admin: bool = is_admin

class Destino:
    def __init__(self, identificador, nombre, descripcion, actividades, precio):
        self.identificador: int = identificador
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.actividades: list = actividades
        self.precio: int = precio

    def __str__(self):
        return f"Destino(identificador={self.identificador}, nombre={self.nombre}, descripcion={self.descripcion}, actividades={self.actividades}, precio={self.precio})"

class Paquete:
    def __init__(self, identificador, nombre, destinos, precio_total):
        self.identificador = identificador
        self.nombre = nombre
        self.destinos = destinos
        self.precio_total = precio_total

    def __str__(self):
        return f"Paquete(identificador={self.identificador}, nombre={self.nombre}, destinos={self.destinos}, precio_total={self.precio_total})"

class Reserva:
    def __init__(self, identificador, id_paquete, id_usuario):
        self.identificador: int = identificador
        self.id_paquete: int = id_paquete
        self.id_usuario: int = id_usuario

    def __str__(self):
        return f"Reserva(identificador={self.identificador}, id_paquete={self.id_paquete}, id_usuario={self.id_usuario})"
