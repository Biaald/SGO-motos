from database import conectar

def buscar_usuario(usuario, senha):

    conn = conectar()

    user = conn.execute(

        "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?",

        (usuario, senha)

    ).fetchone()

    conn.close()

    return user


def buscar_usuario_existente(usuario):

    conn = conectar()

    existe = conn.execute(

        "SELECT * FROM usuarios WHERE usuario = ?",

        (usuario,)

    ).fetchone()

    conn.close()

    return existe


def criar_usuario(
    usuario,
    senha,
    tipo,
    nome,
    telefone,
    email
):

    conn = conectar()

    conn.execute(

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
            usuario,
            senha,
            tipo,
            nome,
            telefone,
            email
        )

    )

    conn.commit()

    conn.close()


def listar_usuarios(busca=None):

    conn = conectar()

    if busca:

        usuarios = conn.execute(

            """

            SELECT

                id,
                nome,
                usuario,
                email,
                telefone,
                tipo

            FROM usuarios

            WHERE nome LIKE ?

            ORDER BY id DESC

            """,

            (f"%{busca}%",)

        ).fetchall()

    else:

        usuarios = conn.execute(

            """

            SELECT

                id,
                nome,
                usuario,
                email,
                telefone,
                tipo

            FROM usuarios

            ORDER BY id DESC

            """

        ).fetchall()

    conn.close()

    return usuarios