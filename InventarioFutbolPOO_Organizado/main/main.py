from controladores.inventario import Inventario
from clases.balon_futbol import BalonFutbol
from clases.bota_futbol import BotaFutbol
from clases.camiseta_futbol import CamisetaFutbol

def main():
    inventario = Inventario()

    # Agregar productos
    balon = BalonFutbol("UM001", "balon de futbol profesional", 50.0, 30, "5", "cuero", "adidas")
    bota = BotaFutbol("UM002", "bota de Futbol para cesped", 120.0, 15, 42, "sintetico", "suelo mojado")
    camiseta = CamisetaFutbol("UM003", "camiseta oficial Futbol", 35.0, 50, "M", "blanca", "once caldas")

    inventario.agregar_producto(balon)
    inventario.agregar_producto(bota)
    inventario.agregar_producto(camiseta)

    print("\n--- Listar Todos los Productos ---")
    inventario.listar_productos()

    print("\n--- Buscar Producto BF001 ---")
    producto = inventario.buscar_producto("BF001")
    if producto:
        producto.mostrar_detalles()

    print("\n--- Actualizar cantidad de BF002 ---")
    inventario.actualizar_cantidad("BF002", 14)

    print("\n--- listar Botas de futbol ---")
    inventario.listar_productos_por_tipo("BotaFutbol")

if __name__ == "__main__":
    main()
