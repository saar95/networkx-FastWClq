from flask import Flask, render_template, request
from url_to_graph import clique_to_sheet
app = Flask(__name__)

@app.route('/')
def action():
    return render_template('layout.html')


@app.route('/', methods=['GET', 'POST'])
def get_data():
    url = request.form.get('url')
    clique_to_sheet('Input')
    return


if __name__ == '__main__':
    app.run(debug=False)
