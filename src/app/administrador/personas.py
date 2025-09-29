from src.app.animales.animal import Animals
class Administrador(Animals):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def ingresar_juguete(self, juguete):
        return f"Administrador {self.nombre} ha ingresado el juguete: {juguete.descripcion_juguete()}"
    
    def cita_veterinaria(self, fecha, hora):
        return Animals.cita_veterinaria(self, fecha, hora)
    def mostrar_citas(self, citas):
        pass
    def reasignar_cita(self, cita_vieja, cita_nueva):
        pass
    def crear_nuevo_usuario(self, nombre, edad):
        nuevo_usuario = Administrador(nombre, edad)
        return f"Nuevo usuario creado: {nuevo_usuario.nombre}, Edad: {nuevo_usuario.edad}"
    def eliminar_usuario(self, usuario):
        return f"Usuario {usuario.nombre} eliminado"
    