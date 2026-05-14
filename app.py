from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    # 1. Definimos las 3 variables (Punto 2 de tu tarea)
    titulo_pagina = "Panel de Control"
    nombre_usuario = "Sophia"
    temas_vistos = ["Rutas", "Plantillas", "Variables"]
   
    # 2. Las pasamos al template (Punto 3 de tu tarea)
    return render_template('index.html',
                           titulo=titulo_pagina,
                           usuario=nombre_usuario,
                           temas=temas_vistos)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/index3')
def index3():
    return render_template('index3.html')

if __name__ == '__main__':
    # Ejecutamos el servidor en modo debug
    app.run(debug=True)
