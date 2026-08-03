from src.database.conexao import conectar

def listar():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM estados_os ORDER BY ordem")
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def listar_ativos():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM estados_os WHERE ativo = 1 ORDER BY ordem")
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def buscar_por_id(id_estado):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM estados_os WHERE id_estado = %s", (id_estado,))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado

def buscar_por_nome(nome):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM estados_os WHERE nome = %s", (nome,))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado

def inserir(estado):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO estados_os (nome, descricao, ordem, ativo) VALUES (%s, %s, %s, %s)"
    valores = (estado.nome, estado.descricao, estado.ordem, estado.ativo)
    cursor.execute(sql, valores)
    conexao.commit()
    estado.id_estado = cursor.lastrowid
    cursor.close()
    conexao.close()
    return estado

def atualizar(estado):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """UPDATE estados_os SET nome=%s, descricao=%s, ordem=%s, ativo=%s
             WHERE id_estado=%s"""
    valores = (estado.nome, estado.descricao, estado.ordem, estado.ativo, estado.id_estado)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def alterar_status(id_estado, novo_status):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE estados_os SET ativo=%s WHERE id_estado=%s", (novo_status, id_estado))
    conexao.commit()
    cursor.close()
    conexao.close()

def contar_os_por_estado(id_estado):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM estados_os WHERE id_estado = %s", (id_estado,))
    total = cursor.fetchone()[0]
    cursor.close()
    conexao.close()
    return total