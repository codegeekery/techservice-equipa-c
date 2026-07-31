from src.database.conexao import conectar

def adicionar_estado(nome, descricao, ordem, ativo):
    conn = conectar()
    cursor = conn.cursor()

    sql = """
    INSERT INTO estados_os (nome, descricao, ordem, ativo)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (nome, descricao, ordem, ativo))
    conn.commit()

    print("Estado cadastrado com sucesso!")

    cursor.close()
    conn.close()