class Persona ():
    def __init__(self,nombre, apellido, edad, ocupacion):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.ocupacion=ocupacion
    def saluda (self):
        return f"hola, soy {self.nombre} {self.apellido}"