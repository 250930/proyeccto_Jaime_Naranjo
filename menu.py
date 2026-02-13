
import json


with open("usuarios.json", "r") as arch:
    usuarios = json.load(arch)

with open("herramientas.json", "r") as arch:
    herramientas = json.load(arch)

def menu_usuarios():

    while True:
        print("""
    ================================
        BIENVENIDO AL MENU DE USUARIO
    ================================
    1. Ver herramientas disponibles
    2. Solocitar prestamo de herramienta
    3. Devolver herramienta
    4. Salir
    ================================
        
        """)
        from herramientas import ver_herramientas_disponibles, solcitar_herramienta, devolver_herramienta
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            ver_herramientas_disponibles(herramientas)       
        elif opcion == "2":
            solcitar_herramienta()
        elif opcion == "3":
            devolver_herramienta()
        elif opcion == "4":
            print("Saliendo del menu de usuario...")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")





def menu_admin():

    while True:
        print("""
    ===============================
        BIENVENIDO MENU ADMINISTRADOR
    ===============================
    1. Ver herramientas disponibles
    2. Agregar herramienta
    3. Modificar herramienta
    4. Eliminar herramienta
    5. Agregar/Actualizar usuario
    6. Prestamos pendientes
    7. Eliminar usuario
    8.Consultas y reportes
    9.Registro de eventos (logs)
    10. Salir
    ================================
        """)
        op = input("Ingrese una opcion: ")
        from herramientas import ver_herramientas_disponibles,agregar_herramienta,  eliminar_herramienta, modificar_herramienta
        from usurios import agregar_actualizar_usuario, prestamos_pendientes, eliminar_usuario, consultas_reportes, registro_eventos
        if op == "1":
            ver_herramientas_disponibles(herramientas)
        elif op == "2":
            agregar_herramienta(herramientas)
        elif op == "3":
            modificar_herramienta(herramientas)
        elif op == "4":            
            eliminar_herramienta(herramientas)
        elif op == "5":
            agregar_actualizar_usuario(usuarios)
        elif op == "6":
            prestamos_pendientes()
        elif op == "7":
            eliminar_usuario(usuarios)
        elif op == "8":
            consultas_reportes()
        elif op == "9":
            registro_eventos()
        elif op == "10":
            print("Saliendo del menu de administrador...")

            break

        else:
            print("Opcion no valida. Intente de nuevo.")

def inicio():
    while True:
        print("""
        =========================
        PRESTAMO DE HERRAMIENTAS
        =========================
        1. Usuario
        2. Administrador
        3. Salir
        =========================
        """)
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "1":
            nom = input("Ingrese su nombre: ")
            id = input("Ingrese su ID: ")
            

            for datos in usuarios:
                if nom.lower() == datos["nombres"].lower() and id == str(datos["id"]) and datos["tipo_usuario"] == "residente":
                    menu_usuarios()
                    return
            else:
                print("Usuario no encontrado.")

        elif opcion == "2":
            nom = input("Ingrese su nombre: ")
            id = input("Ingrese su ID: ")
            
            for datos in usuarios:
            
                if nom.lower() == datos["nombres"].lower() and id == str(datos["id"]) and datos["tipo_usuario"] == "administrador":
                    menu_admin()
                    return
            else:
                print("Usuario no encontrado.")
            
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")
inicio()

