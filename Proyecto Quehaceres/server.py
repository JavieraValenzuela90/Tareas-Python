"""
Estoy importanto un paquete flask de la clase Flask. Y al ser una clas epuedo crar un 
objeto de esa clase, objeto que llamaremos "app"
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/Bienvenidas", methods = ['GET'])
def mensaje_bienvenida():
    return "Bienvenidas al mundo de Flask!"

@app.route("/Prueba", methods = ['GET'])
def mensaje_prueba():
    return "Hola Javi"

@app.route("/multiplica/<int:num1>", methods = ['GET'])
def multiplica_por_diez(num1):
    total = num1 * 10
    return f"{num1} x 10 = {total}"

@app.route("/multiplica/<int:num1>/<int:num2>", methods = ['GET'])
def multiplica_dos_numeros(num1, num2):
    total = num1 * num2
    return f"{num1} x {num2} = {total}"

@app.route("/", methods = ['GET'])
def home():
    return render_template("index.html", nombre = "Javi", apellido = "Valenzuela")


if __name__ == "__main__":
    app.run(debug = True, port = 5002)