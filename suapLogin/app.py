from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/esqueceusenha.html')
def esqueceu():
    return render_template('esqueceusenha.html')

# @app.route('/acessar', methods = ['POST'])
# def acessar():
#     # user = request.form['user']
#     # password = request.form['senha']
#     return render_template('inicial.html')

@app.route('/inicial.html')
def inicial():
    return render_template('inicial.html')