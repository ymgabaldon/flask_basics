# code for the lesson "jinja templating part 2"
# section 3: lecture 13
# USE THIS CODE IN CONJUNCTION WITH THE HTML PROVIDED

from flask import Flask, render_template, request

app = Flask(__name__)


# como siempre, vamos a limpiar el script para dejar solo la parte que se utiliza. En este caso, un diccionario con
# películas y duraciones

# JINJA TEMPLATES 2.
@app.route('/tables')
def movies_plus():
    movies_dict = {'autopsy of jane doe': 02.14,
                   'neon demon': 3.20,
                   'ghost in a shell': 1.50,
                   'kong: skull island': 3.50,
                   'john wick 2': 02.52,
                   'spiderman - homecoming': 1.48}
    # Por último vamos a poner el esquema de html que vamos a utilizar, el diccionario con los datos y el nombre.
    # Todo lo demás está en el ficher html
    return render_template('table_data.html',
                           movies=movies_dict,
                           name='Santiago')


if __name__ == '__main__':
    app.run(debug=True)
