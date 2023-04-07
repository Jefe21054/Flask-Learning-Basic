from flask import Flask,redirect,url_for,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return '''
        <h1 style="font-size: 64px; color: blue">
            CONTACTO
        </h1>
    '''

@app.route('/nosotros')
def about():
    return '''
        <h1 style="font-size: 64px; color: blue">
            NOSOTROS
        </h1>
    '''

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            return redirect(url_for('dashboard', name=username))
    return ''' 
        <form method="POST" style="background-color: #e6e6e6;" >
        <h3>Ingresa tus datos</h3>
            <input type="text" name="username" /> <br /> <br />
            <input type="password" name="password" /> <br /> <br />
            <button type="submit">Enviar</button>
        </form>
    '''

@app.route('/dashboard/<name>')
@app.route('/dashboard')
def dashboard(name=None):
    if name is not None:
        return f'<h1>Bienvenid@ {name} a tu Dashboard!</h1>'
    return redirect(url_for('login'))