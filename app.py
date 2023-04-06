from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1 style="font-size: 64px; color: blue">
            INICIO
        </h1>
    '''

@app.route('/contact')
def contact():
    return '''
        <h1 style="font-size: 64px; color: blue">
            CONTACTO
        </h1>
    '''

@app.route('/about')
def about():
    return '''
        <h1 style="font-size: 64px; color: blue">
            NOSOTROS
        </h1>
    '''

@app.route('/saludo/<name>/<int:sueldo>')
@app.route('/saludo/<name>')
@app.route('/saludo')
def greetings(name=None, sueldo=None):
    print(name)
    if name != None:
        if sueldo is not None:
            return f'<h1 style="font-size: 64px; color: blue">Hola {name}, tu sueldo es: {(sueldo)*2}</h1>'
        return f'<h1 style="font-size: 64px; color: blue">Hola {name}</h1>'
    else:
        return f'<h1 style="font-size: 64px; color: blue">Hola Desconocido</h1>'