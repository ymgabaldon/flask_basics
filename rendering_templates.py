# incremental source code for the lesson "rendering html templates"
# section 2: lecture 11
# TO USE THIS CODE, YOU NEED THE TEMPLATES FOLDER WITH THE HTML FILE. SEE THE OTHER LINK PROVIDED FOR THE HTML PAGE

from flask import Flask, render_template, request

# He quitado los ejemplos anteriores que están en los otros scripts para dejar solo este ejemplo.
# Se ve que la función render_template  sirve para desplegar un archivo html template. NO lo veo muy útil salvo que
# podamos pasarle variables o algo

app = Flask(__name__)


# rendering templates
@app.route('/temp')
def using_templates():
    return render_template('hello.html')


# Este ejemplo es para ver que el head es el título de la página web y aparce en la pestaña

@app.route('/temp2')
def ejemplo_hola2():
    return render_template('hello_2.html')  #


if __name__ == "__main__":
    app.run(debug=True)
