import flask

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    return 'Test'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)