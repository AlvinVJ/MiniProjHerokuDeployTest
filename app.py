from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello, World! this is a test"

if __name__ == '__main__':
    app.run()