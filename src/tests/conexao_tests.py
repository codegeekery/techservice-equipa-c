# tests/test_conexao.py

from src.database.conexao import conectar

import mysql.connector

def test_conexao_banco():
    """Testa se a conexão com a base de dados MySQL é bem-sucedida."""
    try:
        conexao = conectar()
        
        if conexao.is_connected():
            cursor = conexao.cursor()
            cursor.execute("SELECT 1")
            resultado = cursor.fetchone()
            cursor.close()
            conexao.close()
            
            assert resultado == (1,)
            print("✅ OK: Conexão com a base de dados MySQL bem-sucedida.")
        else:
            raise Exception("Conexão não estabelecida.")
            
    except mysql.connector.Error as erro:
        print(f"❌ ERRO: Falha na conexão com a base de dados: {erro}")
        raise


if __name__ == "__main__":
    test_conexao_banco()