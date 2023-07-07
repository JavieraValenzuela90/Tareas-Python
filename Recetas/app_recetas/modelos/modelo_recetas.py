from app_recetas.config.mysqlconnection import connectToMySQL
from app_recetas.modelos.modelo_usuarios import Usuario
from app_recetas import BASE_DATOS
from flask import flash

class Receta:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.descripcion = data["descripcion"]
        self.instrucciones = data["instrucciones"]
        self.fecha_elaboracion = data["fecha_elaboracion"]
        self.menos_treinta = data["menos_treinta"]
        self.id_usuario = data["id_usuario"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def crear_uno(cls, data):
        query = """
                INSERT INTO recetas(nombre, descripcion, instrucciones, fecha_elaboracion, menos_treinta, id_usuario)
                VALUES (%(nombre)s, %(descripcion)s, %(instrucciones)s, %(fecha_elaboracion)s, %(menos_treinta)s, %(id_usuario)s);
                """
        id_receta = connectToMySQL(BASE_DATOS).query_db(query, data)
        return id_receta

    @classmethod
    def obtener_todas_con_usuario(cls):
        query = """
                SELECT *
                FROM recetas r JOIN usuarios u
                    ON r.id_usuario = u.id;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query)
        lista_recetas = []

        for renglon in resultado:
            receta = Receta(renglon)
            data_usuario = {
                "id" : renglon["u.id"],
                "nombre" : renglon["u.nombre"],
                "apellido" : renglon["apellido"],
                "email" : renglon["email"],
                "password" : renglon["password"],
                "created_at" : renglon["u.created_at"],
                "updated_at" : renglon["u.updated_at"]
            }
            usuario = Usuario(data_usuario)
            receta.usuario = usuario
            lista_recetas.append(receta)

        return lista_recetas

    @staticmethod #qué nos van a pedir validar? la Data
    def validar_formulario_recetas(data):
        es_valido = True
        if len(data["nombre"]) < 3:
            es_valido = False
            flash("Debes proporcionar el nombre de la receta.", "error_nombre")
        if len(data["descripcion"]) < 3:
            es_valido = False
            flash("Debes proporcionar la descripcion de la receta.", "error_descripcion")
        if len(data["instrucciones"]) < 3:
            es_valido = False
            flash("Debes proporcionar las instrucciones de la receta.", "error_instrucciones")
        if data["fecha_elaboracion"] == "":
            es_valido = False
            flash("Debes proporcionar la fecha de elaboración de la receta.", "error_fecha_elaboracion")
        if "menos_treinta" not in data:
            es_valido = False
            flash("Debes establecer si la receta se elabora en menos de 30 minutos.", "error_menos_treinta")
        return es_valido