class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_detalles(self):
        print(f"codigo: {self.codigo}, nombre: {self.nombre}, precio: {self.precio}, cantidad: {self.cantidad}")
