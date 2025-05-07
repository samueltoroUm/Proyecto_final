from clases.producto import Producto

class BalonFutbol(Producto):
    def __init__(self, codigo, nombre, precio, cantidad, tamaño, material, marca):
        super().__init__(codigo, nombre, precio, cantidad)
        self.tamaño = tamaño
        self.material = material
        self.marca = marca

    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f"tamaño: {self.tamaño}, material: {self.material}, marca: {self.marca}")
