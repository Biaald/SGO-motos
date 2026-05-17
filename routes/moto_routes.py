from flask import Blueprint, render_template, request, redirect, url_for, session

from services.moto_service import *
from services.produto_service import *

moto = Blueprint("moto", __name__)

# =========================
# CLIENTE
# =========================

@moto.route("/cliente")
def cliente():

    if "usuario" not in session:

        return redirect(url_for("auth.login"))

    produtos = listar_produtos()

    motos = listar_motos_usuario(
        session["usuario"]
    )

    return render_template(

        "cliente.html",

        produtos=produtos,
        motos=motos

    )

# =========================
# REGISTRAR MOTO
# =========================

@moto.route("/registrar_moto", methods=["POST"])
def registrar_moto_cliente():

    if "usuario" not in session:

        return redirect(url_for("auth.login"))

    modelo = request.form["modelo"]

    marca = request.form["marca"]

    placa = request.form["placa"]

    ano = request.form["ano"]

    usuario = session["usuario"]

    registrar_moto(
        usuario,
        modelo,
        marca,
        placa,
        ano
    )

    return redirect(url_for("moto.cliente"))

# =========================
# MOTOS ADMIN
# =========================

@moto.route("/motos")
def motos():

    if "usuario" not in session:

        return redirect(url_for("auth.login"))

    if session["tipo"] != "admin":

        return "Acesso negado"

    motos = listar_motos()

    return render_template(
        "motos.html",
        motos=motos
    )

# =========================
# REMOVER MOTO
# =========================

@moto.route("/remover_moto/<int:id>")
def remover_moto_admin(id):

    if session["tipo"] != "admin":

        return "Acesso negado"

    remover_moto(id)

    return redirect(url_for("moto.motos"))