
# code for the lesson "jinja templating part 1"
# section 3: lecture 12
# USE THIS CODE IN CONJUNCTION WITH THE HTML PROVIDED

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def hello_flask():
    return 'Hello Flask'


@app.route('/new/')
def query_string(greeting='hello'):
    query_val = request.args.get('greeting', greeting)
    return '<h1> the greeting is: {0} </h1>'.format(query_val)


@app.route('/user')
@app.route('/user/<name>')
def no_query_strings(name='mina'):
    return '<h1> hello there ! {} </>'.format(name)


# strings
@app.route('/text/<string:name>')
def working_with_strings(name):
    return '<h1> here is a string: ' + name + '</h1>'


# numbers
@app.route('/numbers/<int:num>')
def working_with_numbers(num):
    return '<h1> the number you picked is: ' + str(num) + '</h1>'


# add numbers
@app.route('/add/<int:num1>/<int:num2>')
def adding_integers(num1, num2):
    return '<h1> the sum is : {}'.format(num1 + num2) + '</h1>'


# floats
@app.route('/product/<float:num1>/<float:num2>')
def product_two_numbers(num1, num2):
    return '<h1> the product is : {}'.format(num1 * num2) + '</h1>'


# rendering templates
@app.route('/temp')
def using_templates():
    return render_template('hello.html')


# JINJA TEMPLATES
@app.route('/watch')
def top_movies():
    movie_list = ['autopsy of jane doe',
                  'neon demon',
                  'ghost in a shell',
                  'kong: skull island',
                  'john wick 2',
                  'spiderman - homecoming']

    return render_template('movies.html',
                           movies=movie_list,
                           name='Harry')


if __name__ == '__main__':
    app.run(debug=True)