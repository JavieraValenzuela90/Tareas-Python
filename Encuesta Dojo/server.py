from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key="esto es secreto"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process',methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/resultados')

@app.route('/resultados')
def resultados():
    return render_template('resultados.html')
    
if __name__=="__main__":
    app.run(debug=True)