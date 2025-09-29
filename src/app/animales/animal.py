class Animals(0):
    def __init__(self, name, species, concentrado=None):
        self.name = name
        self.species = species
        self.concentrado = concentrado
    def registro_animal(self):
        return f"Animal registrado: {self.name}, Especie: {self.species}, Concentrado: {self.concentrado if self.concentrado else 'No asignado'}"
    def cita_veterinaria(self, fecha, hora):
        return f"Cita veterinaria para {self.name} el {fecha} a las {hora}"  
    def historial_medico(self):
        return f"Historial médico de {self.name}"
    def comprar_concentrado(self, concentrado):
        self.concentrado = concentrado
        return f"{self.name} ha comprado el concentrado: {self.concentrado}"
      
    