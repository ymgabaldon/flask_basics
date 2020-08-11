# incremental code - jinja2 filters
# SECTION 3: LECTURE 15

from flask import Flask, render_template, request

app = Flask(__name__)




# JINJA2 - FILTERS
@app.route('/filters')
def filter_data():
    movies_dict = {'autopsy of jane doe': 02.14,
                   'neon demon': 3.20,
                   'ghost in a shell': 1.50,
                   'kong: skull island': 3.50,
                   'john wick 2': 02.52,
                   'spiderman - homecoming': 1.48}

    return render_template('filter_data.html',
                           movies=movies_dict,
                           name=None,
                           film='a christmas carol')


if __name__ == '__main__':
    app.run(debug=True)