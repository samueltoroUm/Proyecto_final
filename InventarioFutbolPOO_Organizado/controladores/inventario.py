class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"producto agregado: {producto.nombre}")

    def eliminar_producto(self, codigo):
        self.productos = [p for p in self.productos if p.codigo != codigo]
        print(f"producto eliminado: {codigo}")

    def buscar_producto(self, codigo):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        print(f"no se encontro el producto con ese codigo {codigo}")
        return None

    def actualizar_cantidad(self, codigo, cantidad):
        p = self.buscar_producto(codigo)
        if p:
            p.cantidad = cantidad
            print(f"cantidad actualizada: {p.nombre} ahora tiene {cantidad} unidades")

    def listar_productos(self):
        for p in self.productos:
            p.mostrar_detalles()

    def listar_productos_por_tipo(self, tipo):
        for p in self.productos:
            if p.__class__.__name__ == tipo:
                p.mostrar_detalles()
