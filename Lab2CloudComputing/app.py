from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route("/add", methods=['POST'])
def add():



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
