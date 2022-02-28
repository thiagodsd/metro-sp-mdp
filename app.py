from flask import (
    Flask,
    render_template,
    request
)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index')
def form_input():
    return render_template('index.html')


@app.route('/resolve', methods=['post'])
def predict():
    metro_from = request.form['metro_from']
    metro_to = request.form['metro_to']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443)