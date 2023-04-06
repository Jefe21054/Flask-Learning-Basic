from flask import Flask

app = Flask(__name__)

@app.route('/hola')
def hola():
    return '''
        <h1 style="font-size: 64px; color: blue">
            Hola Mundo desde Flask!
        </h1>
    '''

if __name__ == '__main__':
    app.run(debug=True)
