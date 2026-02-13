import  json


def ver_herramientas_disponibles(datos):
    if not datos:
        print("No hay herramientas disponibles.")
        return

    print("\n" + "="*90)
    print(f"{'ID':<5} {'NOMBRE':<50} {'CATEGORIA':<15} {'DISP.':<8} {'ESTADO':<20} {'VALOR':<10}")
    print("="*90)

    for herramienta in datos:
        print(f"{herramienta['id']:<5} "
            f"{herramienta['nombre']:<50} "
            f"{herramienta['categoria']:<15} "
            f"{herramienta['cantidad_disponible']:<8} "
            f"{herramienta['estado']:<20} "
            f"{herramienta['valor_estimado']:<10}")

    print("="*90)

        
def agregar_herramienta(herramientas):
    with open("herramientas.json", "r") as arch:
        datos = json.load(arch)

    id_herramienta = str(input("Ingrese el ID de la herramienta: "))
    for herramienta in datos:
        if herramienta["id"] == id_herramienta:
            print("El ID ya existe.")
            return
    nombre = input("Ingrese el nombre de la herramienta: ")
    categoria = input("Ingrese la categoria de la herramienta: ")
    cantidad_disponible = int(input("Ingrese la cantidad disponible de la herramienta: "))
    estado = input("Ingrese el estado de la herramienta: ")
    valor_estimado = float(input("Ingrese el valor estimado de la herramienta: "))
    nueva_herramienta = {
        "id": id_herramienta,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad_disponible": cantidad_disponible,
        "estado": estado,
        "valor_estimado": valor_estimado
    }
    datos.append(nueva_herramienta)
    with open("herramientas.json", "w") as arch:
        json.dump(datos, arch, indent=4)
def modificar_herramienta(herramientas ):
    with open("herramientas.json", "r") as arch:
        datos = json.load(arch)
        id_herramienta = input("Ingrese el ID de la herramienta a modificar: ")
        for herramienta in datos:
            if herramienta["id"] == id_herramienta:
                print("Ingrese los nuevos datos de la herramienta (deje en blanco para mantener el valor actual):")
                nombre = input(f"Nombre ({herramienta['nombre']}): ") or herramienta['nombre']
                categoria = input(f"Categoria ({herramienta['categoria']}): ") or herramienta['categoria']
                cantidad_disponible = input(f"Cantidad disponible ({herramienta['cantidad_disponible']}): ") or herramienta['cantidad_disponible']
                estado = input(f"Estado ({herramienta['estado']}): ") or herramienta['estado']
                valor_estimado = input(f"Valor estimado ({herramienta['valor_estimado']}): ") or herramienta['valor_estimado']

                herramienta.update({
                    "nombre": nombre,
                    "categoria": categoria,
                    "cantidad_disponible": int(cantidad_disponible),
                    "estado": estado,
                    "valor_estimado": float(valor_estimado)
                })
                with open("herramientas.json", "w") as arch:
                    json.dump(datos, arch, indent=4)
                print("Herramienta modificada exitosamente.")
                return
def eliminar_herramienta():
    pass
def solcitar_herramienta():
    pass
def devolver_herramienta():
    pass