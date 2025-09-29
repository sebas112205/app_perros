class Cliente:
    def __init__(self, nombre, edad, id):
        self.nombre = nombre
        self.edad = edad
        self.id = id
    def solicitar_cita(self, animal, fecha, hora):
        return f"Cliente {self.nombre} ha solicitado una cita para {animal.name} el {fecha} a las {hora}"
    def comprar_juguete(self, juguete):
        return f"Cliente {self.nombre} ha comprado el juguete: {juguete.descripcion_juguete()}"
    