from flask import Flask, redirect

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

@app.route('/login/<name>')
@app.route('/login')
def greetings(name=None):
    if name != None:
        return redirect(f'/dashboard/{name}')
    else:
        return f'<h1 style="font-size: 64px; color: blue">Por favor Ingresa tu nombre en la URL...</h1>'

@app.route('/dashboard/<name>')
@app.route('/dashboard')
def dashboard(name=None):
    if name is not None:
        return f'<h1>Bienvenido {name} a tu Dashboard!</h1>'
    # return redirect('/login')
    return redirect('https://duckduckgo.com')