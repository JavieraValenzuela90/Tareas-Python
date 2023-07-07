from app_recetas.config.mysqlconnection import connectToMySQL
from app_recetas import BASE_DATOS, EMAIL_REGEX
from flask import flash

class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def obtener_uno_con_email(cls, data):
        query = """
                SELECT *
                FROM usuarios
                WHERE email = %(email)s;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, data)
        if len(resultado) == 0:
            return None
        else:
            return Usuario(resultado[0])

    @classmethod
    def crear_uno(cls, data):
        query = """
                INSERT INTO usuarios(nombre, apellido, email, password)
                VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);
                """
        id_usuario = connectToMySQL(BASE_DATOS).query_db(query, data)
        return id_usuario

    @staticmethod #qué nos van a pedir validar? la Data
    def validar_registro(data, usuario_existe):
        es_valido = True
        if len(data["nombre"]) < 2:
            es_valido = False
            flash("Tu nombre debe contener al menos 2 carácteres.", "error_nombre")
        if len(data["apellido"]) < 2:
            es_valido = False
            flash("Tu nombre debe contener al menos 2 carácteres.", "error_apellido")
        if not EMAIL_REGEX.match(data["email"]):
            es_valido = False
            flash("Por favor, proporciona un email válido.", "error_email")
        if data["password"] != data["confirmacion_password"]:
            es_valido = False
            flash("Tus password no coinciden.", "error_password")
        if usuario_existe != None:
            es_valido = False
            flash("Este email ya está en uso.", "error_email")
        return es_valido