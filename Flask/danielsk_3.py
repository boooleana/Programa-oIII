from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def padrao():
    return "<a href=http://0.0.0.0:5000/abrir_form_login>form login</a>"

@app.route("/abrir_form_login")
def abrir_form_login():
    return render_template("danielsk_3_login.html")

def verificar_validacao(log, sen):
    return log == "admin" and sen == "123"

@app.route("/processar_login", methods=["POST"])
def processar_login():
    try:
        login = request.form["login"]
        senha = request.form["senha"]
        if verificar_validacao(login, senha):
            return render_template("danielsk_03_menu.html", nome_do_usuario=login)
        else:
            return "login errado, <a href=http://0.0.0.0:5000/abrir_form_login>form login</a>"
    except Exception as e:
        return "404"+(str(e))

app.run(host="0.0.0.0", debug = True)
