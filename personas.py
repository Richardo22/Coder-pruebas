class Persona ():
    def __init__(self,nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
    def saluda (self):
        return f"hola, soy {self.nombre}"