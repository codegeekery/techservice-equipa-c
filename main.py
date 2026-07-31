def menu_estados():
    print("\n" + "=" * 40)
    print("      GESTAO DE ESTADOS DE O.S.       ")
    print("=" * 40)
    print(" 1. Listar todos os Estados")
    print(" 2. Criar novo Estado")
    print(" 3. Buscar Estado por ID")
    print(" 4. Atualizar Estado")
    print(" 5. Eliminar Estado")
    print(" 0. Voltar / Sair")
    print("=" * 40)

def opcao_listar():
    print("\n--- [1] Lista de Estados ---")
    print("A carregar lista de estados...")

def opcao_criar():
    print("\n--- [2] Criar Novo Estado ---")
    nome = input("Digite o nome do novo estado (ex: Em Processamento): ").strip()
    if nome:
        print(f"✅ Estado '{nome}' criado com sucesso!")
    else:
        print("❌ O nome do estado não pode estar vazio.")

def opcao_buscar():
    print("\n--- [3] Buscar Estado por ID ---")
    try:
        estado_id = int(input("Digite o ID do estado: "))
        print(f"A procurar estado com ID {estado_id}...")
    except ValueError:
        print("❌ Por favor, digite um número válido.")

def opcao_atualizar():
    print("\n--- [4] Atualizar Estado ---")
    try:
        estado_id = int(input("Digite o ID do estado a atualizar: "))
        novo_nome = input("Digite o novo nome para o estado: ").strip()
        print(f"✅ Estado ID {estado_id} atualizado para '{novo_nome}'!")
    except ValueError:
        print("❌ ID inválido.")

def opcao_eliminar():
    print("\n--- [5] Eliminar Estado ---")
    try:
        estado_id = int(input("Digite o ID do estado a eliminar: "))
        confirmacao = input(f"Tem a certeza que deseja eliminar o ID {estado_id}? (s/n): ").lower()
        if confirmacao == 's':
            print(f"🗑️ Estado ID {estado_id} eliminado!")
        else:
            print("Operação cancelada.")
    except ValueError:
        print("❌ ID inválido.")

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
            opcao_eliminar()
        elif opcao == "0":
            print("\nA sair da Gestão de Estados...")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()