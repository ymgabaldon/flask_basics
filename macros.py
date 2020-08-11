

from flask import Flask, render_template, request

app = Flask(__name__)
# python code for SECTION 3: LECTURE 16

# JINJA2 - MACROS Se explica cómo utilizar funciones con jinja2 en htmel. aquí solo se pasa un diccionario, nada más.
@app.route('/macros')
def jinja_macros():
    movies_dict = {'autopsy of jane doe': 02.14,
                   'neon demon': 3.20,
                   'ghost in a shell': 1.50,
                   'kong: skull island': 3.50,
                   'john wick 2': 02.52,
                   'spiderman - homecoming': 1.48}

    return render_template('using_macros.html', movies=movies_dict)


if __name__ == '__main__':
    app.run(debug=True)