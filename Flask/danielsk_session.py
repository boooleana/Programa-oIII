from flask import Flask, render_template, request, session
app = Flask(__name__)
app.config["SECRET_KEY"] = "boolean"

@app.route("/")
def padrao():
    return "<a href=/abrir_form_login>Login</a>" +\
           "<br/><a href=/menu>Menu</a>"

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
            session["usuario"] = login
            return abrir_menu()
        else:
            return abrir_pagina_erro("Login e/ou senha incorreto(s).", "abrir_form_login")
    except Exception as e:
        return "404 "+(str(e))

@app.route("/menu")
def abrir_menu():
    return render_template("danielsk_03_menu.html")

@app.route("/logout")
def logout():
    session.pop("usuario")
    return abrir_form_login()

def abrir_pagina_erro(m, link_continuar):
    return render_template("danielsk_erro.html", msg_erro = m, url_continuar = link_continuar)

app.run(host="0.0.0.0", debug = True)
