from src.database.conexao import conectar

def adicionar(estado):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO estados_os 
        (nome, descricao, ordem, ativo)
        VALUES (%s, %s, %s, %s)
    """

    valores = (
        estado.get_nome(),
        estado.get_descricao(),
        estado.get_ordem(),
        estado.get_ativo()
    )

    cursor.execute(sql, valores)
    conexao.commit()

    estado.id_estado = cursor.lastrowid

    cursor.close()
    conexao.close()

    return estado

def listar_estado(id_estado):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM estados_os
        WHERE id_estado = %s
    """

    cursor.execute(sql, (id_estado,))

    estado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return estado

def atualizar(estado):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE estados_os
        SET nome=%s,
            descricao=%s,
            ordem=%s,
            ativo=%s
        WHERE id_estado=%s
    """

    valores = (
        estado.get_nome(),
        estado.get_descricao(),
        estado.get_ordem(),
        estado.get_ativo(),
        estado.get_id_estado()
    )

    cursor.execute(sql, valores)

    conexao.commit()

    cursor.close()
    conexao.close()

    return estado

def eliminar_estado(id_estado):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        DELETE FROM estados_os
        WHERE id_estado = %s
    """

    cursor.execute(sql, (id_estado,))

    conexao.commit()

    cursor.close()
    conexao.close()

