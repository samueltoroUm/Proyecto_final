from clases.producto import Producto

class CamisetaFutbol(Producto):
    def __init__(self, codigo, nombre, precio, cantidad, tamaño, color, equipo):
        super().__init__(codigo, nombre, precio, cantidad)
        self.tamaño = tamaño
        self.color = color
        self.equipo = equipo

    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f"tamasño: {self.tamaño}, color: {self.color}, equipo: {self.equipo}")
