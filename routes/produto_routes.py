from flask import Blueprint, render_template, request, redirect, url_for, session

from services.produto_service import *

produto = Blueprint("produto", __name__)

# =========================
# INÍCIO
# =========================

@produto.route("/")
def inicio():

    busca = request.args.get("busca")

    produtos = listar_produtos(busca)

    return render_template(
        "index.html",
        produtos=produtos
    )

# =========================
# ADMIN
# =========================

@produto.route("/admin")
def admin():

    if "usuario" not in session:

        return redirect(url_for("auth.login"))

    if session["tipo"] != "admin":

        return "Acesso negado"

    produtos = listar_produtos()

    total_produtos = len(produtos)

    valor_total = 0

    for p in produtos:

        valor_total += p["preco"] * p["quantidade"]

    return render_template(

        "admin.html",

        produtos=produtos,
        total_produtos=total_produtos,
        valor_total=valor_total

    )

# =========================
# PRODUTOS
# =========================

@produto.route("/adicionar", methods=["POST"])
def adicionar():

    if session["tipo"] != "admin":

        return "Acesso negado"

    nome = request.form["nome"]

    quantidade = int(
        request.form["quantidade"]
    )

    preco = float(
        request.form["preco"]
    )

    adicionar_produto(
        nome,
        quantidade,
        preco
    )

    return redirect(url_for("produto.admin"))

@produto.route("/remover/<int:id>")
def remover(id):

    if session["tipo"] != "admin":

        return "Acesso negado"

    remover_produto(id)

    return redirect(url_for("produto.admin"))

@produto.route("/aumentar/<int:id>")
def aumentar(id):

    aumentar_produto(id)

    return redirect(url_for("produto.admin"))

@produto.route("/diminuir/<int:id>")
def diminuir(id):

    diminuir_produto(id)

    return redirect(url_for("produto.admin"))