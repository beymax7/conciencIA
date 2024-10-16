from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quienes-somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        # Aquí puedes manejar los datos del formulario, como guardarlos o enviarlos por correo.
        print(f'Nombre: {nombre}, Correo: {correo}, Mensaje: {mensaje}')
        return render_template('contacto.html', success=True)  # Renderiza la página de contacto y muestra un mensaje de éxito

    return render_template('contacto.html', success=False)

if __name__ == '__main__':
    app.run(debug=True)

