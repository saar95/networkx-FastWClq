from flask import Flask, render_template, request
from url_to_graph import clique_to_sheet
app = Flask(__name__)
app.config["SECRET_KEY"] = "RandomString"
message = "Great job, We opened new spreadsheet in the google docs named Output with your result. (Link: https://docs.google.com/spreadsheets/d/1ysyLfMkiOadNudJkpyUz-wAVPpKcCK9CXqu9hnQGxrA/edit#gid=0"


@app.route('/')
def action():
    return render_template('home_layout.html')


@app.route('/', methods=['GET', 'POST'])
def get_data():
    url = request.form.get('url')
    clique_to_sheet('Input',url)
    return message


if __name__ == '__main__':
    app.run(debug=False)
