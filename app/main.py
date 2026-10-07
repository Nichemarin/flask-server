from flask import Flask, render_template, url_for

# Inicializamos la aplicación
app = Flask(__name__)


productos = [{"nombre": "Teclado mecanico", "precio": 49.99, "disponible": True}, 
                 {"nombre": "Raton", "precio": 29.99, "disponible": False}, 
                 {"nombre": "Monitor 4K", "precio": 69.99, "disponible": True}]
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
    return render_template("saludo.html", name=name)

@app.route("/multiplicar/<int:num1>/<int:num2>")
def numltiplicar(num1, num2):
    return (
        f"<h3>Al multiplicar {num1} y {num2} nos da como resultado {num1 * num2}</h3>"
    )


@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html", nombre="algo", lista_productos = productos)

@app.route("/catalogo/<int:idProducto>")
def producto(idProducto):
    return render_template("productos.html", idProducto = idProducto, producto=productos[idProducto])

if __name__ == "__main__":
    # host='0.0.0.0' es VITAL en Docker para que el servidor sea accesible desde fuera del contenedor
    # debug=True hará que el servidor se reinicie automáticamente si cambias este archivo
    app.run(host="0.0.0.0", port=5000, debug=True)
