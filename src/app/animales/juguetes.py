class Juguetes:
    def __init__(self, tipo, material, precio,id):
        self.tipo = tipo
        self.material = material
        self.precio = precio
        self.id = id

    def descripcion_juguete(self,):
        return f"Juguete: {self.tipo}, Material: {self.material}, Precio: ${self.precio}"
