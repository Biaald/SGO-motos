from flask import Blueprint, render_template, request, redirect, url_for, session

from repositories.usuario_repository import listar_usuarios

usuario = Blueprint("usuario", __name__)

# =========================
# USUÁRIOS
# =========================

@usuario.route("/usuarios")
def usuarios():

    if "usuario" not in session:

        return redirect(url_for("auth.login"))

    if session["tipo"] != "admin":

        return "Acesso negado"

    busca = request.args.get("busca")

    usuarios = listar_usuarios(busca)

    return render_template(
        "usuarios.html",
        usuarios=usuarios
    )