class Juguetes:
    def __init__(self, tipo, material, precio):
        self.tipo = tipo
        self.material = material
        self.precio = precio

    def descripcion_juguete(self):
        list.__add__(Juguetes)
        return f"Juguete: {self.tipo}, Material: {self.material}, Precio: ${self.precio}"