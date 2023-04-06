from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1 style="font-size: 64px; color: blue">
            INICIO
        </h1>
    '''

@app.route('/contacto/')
def contact():
    return '''
        <h1 style="font-size: 64px; color: blue">
            CONTACTO
        </h1>
    '''

@app.route('/nosotros/')
def about():
    return '''
        <h1 style="font-size: 64px; color: blue">
            NOSOTROS
        </h1>
    '''