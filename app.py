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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/index3')
def index3():
    return render_template('index3.html')


@app.route("/inicio2")
def inicio2():
    return render_template("inicio2.html")

@app.route("/acerca")
def acerca():
    return render_template("acerca.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


# Ruta recursos
@app.route("/recursos")
def recursos():

    recursos = [
        "Entorno virtual",
        "Rutas en Flask",
        "Plantillas HTML",
        "Variables con Jinja",
        "Listas y bucles"
    ]

    return render_template("recursos.html", recursos=recursos)
    

if __name__ == '__main__':
    # Ejecutamos el servidor en modo debug
    app.run(debug=True)






