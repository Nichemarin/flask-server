from flask import Flask, render_template

# Inicializamos la aplicación
app = Flask(__name__)


# Ruta 1: Devuelve un HTML muy básico
@app.route("/")
def home():
#   return """
 #       <h1>¡Hola desde Flask en Docker!!!!</h1>
  #      <p>Este es tu primer servidor Python funcionando.</p>
   # """
   return render_template("index.html")


@app.route("/saludo/<name>")
def saludo(name):
    # return f"<h1>Bienvenido a Flask, {name}</h1>"
    return render_template("saludo.html")

@app.route("/multiplicar/<int:num1>/<int:num2>")
def numltiplicar(num1, num2):
    return (
        f"<h3>Al multiplicar {num1} y {num2} nos da como resultado {num1 * num2}</h3>"
    )


@app.route("/catalogo/<int:id_product>")
def catalogo(id_product):
    productos = [{"nombre": "Teclado mecanico", "precio": 49.99, "disponible": True}, 
                 {"nombre": "Raton", "precio": 29.99, "disponible": False}, 
                 {"nombre": "Monitor 4K", "precio": 69.99, "disponible": True}]
    return render_template("catalogo.html", nombre="algo", id_product=id_product, lista_productos = productos)


if __name__ == "__main__":
    # host='0.0.0.0' es VITAL en Docker para que el servidor sea accesible desde fuera del contenedor
    # debug=True hará que el servidor se reinicie automáticamente si cambias este archivo
    app.run(host="0.0.0.0", port=5000, debug=True)
