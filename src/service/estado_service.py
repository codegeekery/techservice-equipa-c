"""
Serviço de Gestão de Estados da Ordem de Serviço (Equipa C)
Responsável pelas regras de negócio, validações e transições de estado das OS.
"""

from typing import List, Dict, Optional
import src.repositories.estados_OS_repository as estado_repo
from src.models.estado import Estado #Placeholder Name


class EstadoService:

    @staticmethod
    def listar_todos_estados() -> List[Dict]:
        """
        Obtém a lista de todos os estados registados no sistema.
        """
        try:
            return estado_repo.listar()
        except Exception as e:
            raise RuntimeError(f"Erro ao carregar os estados: {e}")

    @staticmethod
    def listar_estados_ativos() -> List[Dict]:
        """
        Obtém apenas os estados que estão atualmente ativos (ativo = 1).
        Útil para preencher dropdowns na criação/edição de Ordens de Serviço.
        """
        try:
            return estado_repo.listar_ativos()
        except Exception as e:
            raise RuntimeError(f"Erro ao carregar estados ativos: {e}")

    @staticmethod
    def obter_estado_por_id(id_estado: int) -> Optional[Dict]:
        """
        Busca a informação detalhada de um estado específico através do seu ID.
        """
        if not id_estado or id_estado <= 0:
            raise ValueError("O ID do estado fornecido é inválido.")
            
        try:
            return estado_repo.buscar_por_id(id_estado)
        except Exception as e:
            raise RuntimeError(f"Erro ao buscar estado com ID {id_estado}: {e}")

    @staticmethod
    def criar_estado(nome: str, descricao: str = "", ordem: int = 1) -> Estado:
        """
        Valida os dados e cria um novo estado de OS no sistema.
        """
        nome_limpo = nome.strip() if nome else ""
        
        # Validação de campos obrigatórios
        if not nome_limpo:
            raise ValueError("O nome do estado é obrigatório.")
        
        if len(nome_limpo) < 3:
            raise ValueError("O nome do estado deve ter pelo menos 3 caracteres.")

        # Verificar se já existe um estado com o mesmo nome para evitar duplicados
        estado_existente = estado_repo.buscar_por_nome(nome_limpo)
        if estado_existente:
            raise ValueError(f"Já existe um estado registado com o nome '{nome_limpo}'.")

        # Criar a instância do modelo
        novo_estado = Estado(
            nome=nome_limpo,
            descricao=descricao.strip() if descricao else "",
            ordem=max(1, ordem),
            ativo=1
        )

        try:
            return estado_repo.inserir(novo_estado)
        except Exception as e:
            raise RuntimeError(f"Erro ao guardar o novo estado no banco de dados: {e}")

    @staticmethod
    def atualizar_estado(id_estado: int, nome: str, descricao: str = "", ordem: int = 1, ativo: int = 1) -> None:
        """
        Valida e atualiza as informações de um estado existente.
        """
        if not id_estado or id_estado <= 0:
            raise ValueError("ID de estado inválido para atualização.")

        nome_limpo = nome.strip() if nome else ""
        if not nome_limpo:
            raise ValueError("O nome do estado não pode ficar vazio.")

        # Verificar se o estado existe na base de dados
        estado_atual = estado_repo.buscar_por_id(id_estado)
        if not estado_atual:
            raise ValueError(f"Estado com ID {id_estado} não foi encontrado.")

        # Se o nome mudou, garantir que não colide com outro estado já existente
        if estado_atual['nome'].lower() != nome_limpo.lower():
            conflito = estado_repo.buscar_por_nome(nome_limpo)
            if conflito and conflito['id_estado'] != id_estado:
                raise ValueError(f"Já existe outro estado com o nome '{nome_limpo}'.")

        estado_atualizado = Estado(
            id_estado=id_estado,
            nome=nome_limpo,
            descricao=descricao.strip() if descricao else "",
            ordem=max(1, ordem),
            ativo=ativo
        )

        try:
            estado_repo.atualizar(estado_atualizado)
        except Exception as e:
            raise RuntimeError(f"Erro ao atualizar o estado {id_estado}: {e}")

    @staticmethod
    def alternar_status_ativo(id_estado: int, novo_status: int) -> None:
        """
        Ativa (1) ou desativa (0) um estado no sistema.
        evita a eliminação física para preservar a integridade referencial com ordens_servico.
        """
        if not id_estado or id_estado <= 0:
            raise ValueError("ID de estado inválido.")

        if novo_status not in [0, 1]:
            raise ValueError("O valor de status deve ser 0 (inativo) ou 1 (ativo).")

        # Impedir a desativação de estados que estejam associados a ordens de serviço ativas
        if novo_status == 0:
            qtd_os_vinculadas = estado_repo.contar_os_por_estado(id_estado)
            if qtd_os_vinculadas > 0:
                raise ValueError(
                    f"Não é possível desativar este estado pois existem {qtd_os_vinculadas} "
                    f"Ordem(ns) de Serviço associada(s) a ele."
                )

        try:
            estado_repo.alterar_status(id_estado, novo_status)
        except Exception as e:
            raise RuntimeError(f"Erro ao alterar o status do estado {id_estado}: {e}")

    @staticmethod
    def validar_transicao_estado(id_estado_atual: int, id_novo_estado: int) -> bool:
        """
        Valida se a mudança de um estado para outro é permitida no fluxo de trabalho.
        Útil para impedir saltos ilógicos no ciclo de vida da OS (ex: de 'Aberta' direto para 'Entregue').
        """
        if id_estado_atual == id_novo_estado:
            return True

        novo_estado = estado_repo.buscar_por_id(id_novo_estado)
        if not novo_estado or novo_estado.get('ativo') != 1:
            raise ValueError("O novo estado selecionado é inválido ou está inativo.")

        # As regras específicas de transição podem ser expandidas conforme o fluxo da equipa
        return True