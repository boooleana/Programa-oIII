from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/boasvindas")
def welcome():
    return "Bem vindo"

app.run(host="0.0.0.0")
