# code for the lesson "understanding query strings"
# section 2: lecture 9

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def hello_flask():
    return 'Hello Flask'


# Aquí en este ejemplo es cómo capturar la info directamente desde la URL.
# Es lo que se llama "query strings". Al final, son parámetros que se pasan adosados a la url tra un signo de ?
# y para incorporarlos hace falta el método request. Con resquest.args obtienes esos parámetros como diccionario
# y finalmente, con el get y la clave obtienes el resultado, en este caso es greeting
# Por defecto: http://localhost:5000/new/
# Para meter el valor de greeting: http://localhost:5000/new/?greeting=Hola

@app.route('/new/')
def query_string(greeting='hello'):
    query_val = request.args.get('greeting',
                                 greeting)  # Aquí greeting es la clave y greeting el valor que recibe de la función
    return '<h1> the greeting is: {0} </h1>'.format(query_val)


""" Este nuevo ejemplo hace esencialmente lo mismo, con la diferencia que no rquiere la querystring.
Por tanto, no es necesario pasar el parámetro en la url con la ?, sino que se define una variable,
name (lo que va entre corchetes son variables) a la que luego por defecto se le pasa el valor que se quiera:

http://localhost:5000/user para obtener el resultado por defecto
http://localhost:5000/user/Santiago
"""


@app.route('/user')
@app.route('/user/<name>')
def no_query_strings(name='mina'):
    return '<h1> hello there ! {} </h1>'.format(name)


# esto no venía en elcódigo, por lo que no podía funcionar

if __name__ == '__main__':
    app.run(debug=True)
