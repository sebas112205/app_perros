class Cliente:
    def __init__(self, nombre, edad, id):
        self.nombre = nombre
        self.edad = edad
        self.id = id
    def solicitar_cita(self, animal, fecha, hora):
        return f"Cliente {self.nombre} ha solicitado una cita para {animal.name} el {fecha} a las {hora}"
    def ver_historial(self, animal):
        return f"Mostrando historial médico de {animal.name}"
    def compra(self, animal, concentrado, cantidad, precio,juguete=None):
        return f"Cliente {self.nombre} ha comprado {cantidad} de {concentrado} para {animal.name} por ${precio}" + (f" y el juguete {juguete.descripcion_juguete()}" if juguete else "")