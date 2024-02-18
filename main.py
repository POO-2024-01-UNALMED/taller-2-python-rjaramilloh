class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        color = color.upper
        if color == "ROJO":
            self.color = color
        elif color == "VERDE":
            self.color = color
        elif color == "AMARILLO":
            self.color = color
        elif color == "NEGRO":
            self.color = color
        elif color == "BLANCO":
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        tipo = tipo.upper
        if tipo == "ELECTRICO" or tipo == "GASOLINA":
            self.tipo=tipo

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos 
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        i = 0
        for i in range (0,len(self.asientos)):
            if (type(self.asientos[i]) == Asiento):
                i=i+1
        return i
    
    def verificarIntegridad(self):
        prueba = "Auto original"
        for i in range (0,len(self.asientos)):
            if (type(self.asientos[i]) == Asiento):
                if self.asientos[i].registro != self.registro or self.asientos[i].registro != self.motor.registro:
                        prueba = "Las piezas no son originales"
        return prueba
    