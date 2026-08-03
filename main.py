# main.py
from src.service.estado_service import EstadoService

def menu_estados():
    print("\n" + "=" * 40)
    print("      GESTAO DE ESTADOS DE O.S.       ")
    print("=" * 40)
    print(" 1. Listar todos os Estados")
    print(" 2. Criar novo Estado")
    print(" 3. Buscar Estado por ID")
    print(" 4. Atualizar Estado")
    print(" 5. Ativar/Desativar Estado")
    print(" 0. Voltar / Sair")
    print("=" * 40)

def opcao_listar():
    print("\n--- [1] Lista de Estados ---")
    try:
        estados = EstadoService.listar_todos_estados()
        if not estados:
            print("Nenhum estado registado.")
        for e in estados:
            print(f"ID: {e['id_estado']} | {e['nome']} | ordem={e['ordem']} | ativo={e['ativo']}")
    except (RuntimeError, ValueError) as e:
        print(f"❌ {e}")

def opcao_criar():
    print("\n--- [2] Criar Novo Estado ---")
    nome = input("Nome do novo estado (ex: Em Processamento): ").strip()
    descricao = input("Descrição (opcional): ").strip()
    try:
        ordem = int(input("Ordem (número, padrão 1): ") or 1)
    except ValueError:
        ordem = 1
    try:
        estado = EstadoService.criar_estado(nome, descricao, ordem)
        print(f"✅ Estado '{estado.nome}' criado com sucesso! (ID: {estado.id_estado})")
    except (ValueError, RuntimeError) as e:
        print(f"❌ {e}")

def opcao_buscar():
    print("\n--- [3] Buscar Estado por ID ---")
    try:
        estado_id = int(input("ID do estado: "))
        estado = EstadoService.obter_estado_por_id(estado_id)
        if estado:
            print(estado)
        else:
            print("Estado não encontrado.")
    except ValueError as e:
        print(f"❌ {e}")
    except RuntimeError as e:
        print(f"❌ {e}")

def opcao_atualizar():
    print("\n--- [4] Atualizar Estado ---")
    try:
        estado_id = int(input("ID do estado a atualizar: "))
        nome = input("Novo nome: ").strip()
        descricao = input("Nova descrição (opcional): ").strip()
        ordem = int(input("Nova ordem (padrão 1): ") or 1)
        ativo = int(input("Ativo? 1=sim, 0=não (padrão 1): ") or 1)
        EstadoService.atualizar_estado(estado_id, nome, descricao, ordem, ativo)
        print(f"✅ Estado ID {estado_id} atualizado!")
    except (ValueError, RuntimeError) as e:
        print(f"❌ {e}")

def opcao_alternar_status():
    print("\n--- [5] Ativar/Desativar Estado ---")
    try:
        estado_id = int(input("ID do estado: "))
        novo_status = int(input("Novo status (1=ativo, 0=inativo): "))
        EstadoService.alternar_status_ativo(estado_id, novo_status)
        print(f"✅ Status do estado ID {estado_id} alterado!")
    except (ValueError, RuntimeError) as e:
        print(f"❌ {e}")

def main():
    while True:
        menu_estados()
        opcao = input("Selecione uma opção: ").strip()

        if opcao == "1":
            opcao_listar()
        elif opcao == "2":
            opcao_criar()
        elif opcao == "3":
            opcao_buscar()
        elif opcao == "4":
            opcao_atualizar()
        elif opcao == "5":
            opcao_alternar_status()
        elif opcao == "0":
            print("\nA sair da Gestão de Estados...")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()