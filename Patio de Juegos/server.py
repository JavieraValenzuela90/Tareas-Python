from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play", methods = ['GET'])
def blue_boxes():
    boxes = ''
    for i in range(3):
        boxes += '<div style="background-color:blue;" class="box"></div>'
    return render_template("index.html", boxes = boxes) 

@app.route("/play/<int:x>", methods = ['GET'])
def x_blue_boxes(x):
    boxes = ''
    for i in range(x):
        boxes += '<div style="background-color:blue;" class="box"></div>'
    return render_template("index.html", boxes = boxes) 

@app.route("/play/<int:x>/<color>", methods = ['GET'])
def x_color_boxes(x, color):
    boxes = ''
    for i in range(x):
        boxes += f'<div style="background-color:{color}!important;" class="box"></div>'
    return render_template("index.html", boxes = boxes) 

if __name__ == "__main__":
    app.run(debug = True, port = 5001)


