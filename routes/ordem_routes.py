from flask import Blueprint, render_template, request, redirect, url_for, session

from services.ordem_service import *

ordem = Blueprint("ordem", __name__)

# =========================
# ORDENS
# =========================

@ordem.route("/ordens")
def ordens():

    if "usuario" not in session:

        return redirect(url_for("auth.login"))

    if session["tipo"] == "admin":

        ordens = listar_ordens_admin()

    else:

        ordens = listar_ordens_usuario(
            session["usuario"]
        )

    return render_template(
        "ordens.html",
        ordens=ordens
    )

# =========================
# ADICIONAR ORDEM
# =========================

@ordem.route("/adicionar_ordem", methods=["POST"])
def adicionar_ordem_admin():

    if "usuario" not in session:

        return redirect(url_for("auth.login"))

    if session["tipo"] != "admin":

        return "Acesso negado"

    usuario = request.form["usuario"]

    cliente = request.form["cliente"]

    moto = request.form["moto"]

    servico = request.form["servico"]

    valor = request.form["valor"]

    adicionar_ordem(
        usuario,
        cliente,
        moto,
        servico,
        valor
    )

    return redirect(url_for("ordem.ordens"))

# =========================
# FINALIZAR ORDEM
# =========================

@ordem.route("/finalizar_ordem/<int:id>")
def finalizar_ordem_admin(id):

    if "usuario" not in session:

        return redirect(url_for("auth.login"))

    if session["tipo"] != "admin":

        return "Acesso negado"

    finalizar_ordem(id)

    return redirect(url_for("ordem.ordens"))

# =========================
# REMOVER ORDEM
# =========================

@ordem.route("/remover_ordem/<int:id>")
def remover_ordem_admin(id):

    if "usuario" not in session:

        return redirect(url_for("auth.login"))

    if session["tipo"] != "admin":

        return "Acesso negado"

    remover_ordem(id)

    return redirect(url_for("ordem.ordens"))