class Estado:
    def __init__(
        self, 
        id_estado=None, 
        nome="", 
        descricao="", 
        ordem=0, 
        ativo=1
    ):
        self.id_estado = id_estado
        self.nome = nome
        self.descricao = descricao
        self.ordem = ordem
        self.ativo = ativo

    def __str__(self):
        return f"{self.id_estado} - {self.nome} - {self.descricao} - {self.ordem} - {self.ativo}"