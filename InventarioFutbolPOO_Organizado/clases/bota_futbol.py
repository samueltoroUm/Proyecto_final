from clases.producto import Producto

class BotaFutbol(Producto):
    def __init__(self, codigo, nombre, precio, cantidad, tamaño, material, tipo):
        super().__init__(codigo, nombre, precio, cantidad)
        self.tamaño = tamaño
        self.material = material
        self.tipo = tipo

    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f"tamaño: {self.tamaño}, material: {self.material}, tipo: {self.tipo}")
