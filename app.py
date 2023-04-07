from flask import Flask,redirect,url_for,request,\
    render_template,flash,session
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'so-S3cr3t!'

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
    form = LoginForm()
    if form.validate_on_submit() and request.method == 'POST':
        username = form.username.data
        password = form.password.data
        if username and password:
            session['username'] = username
            return redirect(url_for('dashboard',name=username))
        flash('Por favor, ingresa correctamente tus datos.','error')
    return render_template('login.html',form=form)

@app.route('/dashboard/<name>')
@app.route('/dashboard')
def dashboard(name=None):
    if name is not None:
        flash(f'Bienvenid@ usuario {name}','success')
        return render_template('dashboard.html',username=name)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))