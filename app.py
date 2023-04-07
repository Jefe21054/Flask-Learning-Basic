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
            return redirect(url_for('dashboard',name=username))
    return render_template('login.html')

@app.route('/dashboard/<name>')
@app.route('/dashboard')
def dashboard(name=None):
    if name is not None:
        return render_template('dashboard.html',username=name)
    return redirect(url_for('login'))