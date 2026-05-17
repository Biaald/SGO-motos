from database import conectar

def listar_ordens_admin():

    conn = conectar()

    ordens = conn.execute(

        "SELECT * FROM ordens ORDER BY id DESC"

    ).fetchall()

    conn.close()

    return ordens


def listar_ordens_usuario(usuario):

    conn = conectar()

    ordens = conn.execute(

        """

        SELECT * FROM ordens
        WHERE usuario = ?

        ORDER BY id DESC

        """,

        (usuario,)

    ).fetchall()

    conn.close()

    return ordens


def adicionar_ordem(
    usuario,
    cliente,
    moto,
    servico,
    valor
):

    conn = conectar()

    conn.execute(

        """

        INSERT INTO ordens(
            usuario,
            cliente,
            moto,
            servico,
            valor,
            status
        )

        VALUES (?, ?, ?, ?, ?, ?)

        """,

        (
            usuario,
            cliente,
            moto,
            servico,
            valor,
            "Em andamento"
        )

    )

    conn.commit()

    conn.close()


def finalizar_ordem(id):

    conn = conectar()

    conn.execute(

        """

        UPDATE ordens
        SET status = ?

        WHERE id = ?

        """,

        (
            "Finalizado",
            id
        )

    )

    conn.commit()

    conn.close()


def remover_ordem(id):

    conn = conectar()

    conn.execute(

        "DELETE FROM ordens WHERE id = ?",

        (id,)

    )

    conn.commit()

    conn.close()