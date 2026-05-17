from flask import Flask

from database import conectar

from routes.auth_routes import auth
from routes.produto_routes import produto
from routes.moto_routes import moto
from routes.ordem_routes import ordem
from routes.usuario_routes import usuario

app = Flask(__name__)

app.secret_key = "segredo123"

# TABELAS

conn = conectar()

cursor = conn.cursor()

# USUÁRIOS

cursor.execute("""

CREATE TABLE IF NOT EXISTS usuarios(

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT,
    senha TEXT,
    tipo TEXT,
    nome TEXT,
    telefone TEXT,
    email TEXT

)

""")

# PRODUTOS

cursor.execute("""

CREATE TABLE IF NOT EXISTS produtos(

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    quantidade INTEGER,
    preco REAL

)

""")

# MOTOS

cursor.execute("""

CREATE TABLE IF NOT EXISTS motos(

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT,
    modelo TEXT,
    marca TEXT,
    placa TEXT,
    ano TEXT

)

""")

# ORDENS

cursor.execute("""

CREATE TABLE IF NOT EXISTS ordens(

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT,
    cliente TEXT,
    moto TEXT,
    servico TEXT,
    valor REAL,
    status TEXT

)

""")

conn.commit()


# CRIAR ADMIN

admin = cursor.execute(

    "SELECT * FROM usuarios WHERE usuario = ?",

    ("admin",)

).fetchone()

if not admin:

    cursor.execute(

        """

        INSERT INTO usuarios(
            usuario,
            senha,
            tipo,
            nome,
            telefone,
            email
        )

        VALUES (?, ?, ?, ?, ?, ?)

        """,

        (
            "admin",
            "123",
            "admin",
            "Administrador",
            "000000000",
            "admin@gmail.com"
        )

    )

    conn.commit()

conn.close()

# BLUEPRINTS

app.register_blueprint(auth)

app.register_blueprint(produto)

app.register_blueprint(moto)

app.register_blueprint(ordem)

app.register_blueprint(usuario)


# INICIAR

if __name__ == "__main__":

    app.run(debug=True, port=5001)