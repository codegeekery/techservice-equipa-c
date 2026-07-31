class Estado:

    def __init__(
        self,
        id_estado=None,
        nombre="",
        descripcion="",
        orden=0,
        activo=1
    ):
        self.id_estado = id_estado
        self.nombre = nombre
        self.descripcion = descripcion
        self.orden = orden
        self.activo = activo

    def __str__(self):
        return (
            f"{self.id_estado} - "
            f"{self.nombre} - "
            f"{self.descripcion} - "
            f"{self.orden} - "
            f"{self.activo}"
        )