from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',num = 8,width=8)

@app.route('/<int:num>')
def size(num):
    return render_template('index.html',num=num,width=8)

@app.route('/<int:width>/<int:num>')
def size_xy(width, num):
    return render_template('index.html', width=width, num=num)

@app.route("/<int:width>/<int:num>/<string:color1>/<string:color2>")
def custom(width, num, color1, color2):
    return render_template('index.html', width=width, num=num,color1=color1, color2=color2)

if __name__ == '__main__':
    app.run(debug=True)