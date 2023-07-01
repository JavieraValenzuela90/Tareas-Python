from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", phrase="hola", times=5)# ¡Fíjate en los 2 nuevos argumentos nombrados!

if __name__=="__main__":
    app.run(debug=True)

