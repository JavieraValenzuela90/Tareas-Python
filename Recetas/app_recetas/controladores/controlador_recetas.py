from flask import render_template, redirect, request, session, flash
from app_recetas.modelos.modelo_recetas import Receta
from app_recetas import app

@app.route('/recetas', methods = ['GET'])
def desplegar_recetas():
    lista_recetas = Receta.obtener_todas_con_usuario()    # obtener todas las recetas
    return render_template('recetas.html', lista_recetas = lista_recetas)
    # enviar la lista de recetas hacia el template

@app.route('/formulario/receta', methods = ['GET'])
def desplegar_formulario_receta():
    return render_template('formulario_receta.html')

@app.route("/crear/receta", methods = ['POST'])
def nueva_receta():
    data = {
        **request.form, 
        "id_usuario" : session['id_usuario']
    }
    if Receta.validar_formulario_recetas(data) == False:
        return redirect('/formulario/receta')
    else:
        id_receta = Receta.crear_uno(data) #no olvidar validar formulario
        return redirect('/recetas')
