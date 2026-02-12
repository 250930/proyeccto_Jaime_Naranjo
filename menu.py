
import json 

with open("usuarios.json", "r") as arch:
    usuarios = json.load(arch)




def menu_usuarios():

    while True:
        print("""
        ================================
         BIENVENIDO AL MENU DE USUARIO
        ================================
        1. Ver herramientas disponibles
        2. Prestar herramienta
        3. Devolver herramienta
        4. Salir
        ================================
        
        """)
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            ver_herramientas_disponibles()       
        elif opcion == "2":
            prestar_herramienta()
            pass
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
        2. Agregar/Actualizar herramienta
        3. Eliminar herramienta
        4. Agregar/Actualizar usuario
        5. Prestamos pendientes
        6. Eliminar usuario
        7.Consultas y reportes
        8.Registro de eventos (logs)
        9. Salir
        ================================
        """)
        op = input("Ingrese una opcion: ")
        if op == "1":
            ver_herramientas_disponibles()
        elif op == "2":
            agregar_actualizar_herramienta()
        elif op == "3":
            eliminar_herramienta()
        elif op == "4":
            agregar_actualizar_usuario()
        elif op == "5":
            prestamos_pendientes()
        elif op == "6":
            eliminar_usuario()
        elif op == "7":
            consultas_reportes()
        elif op == "8":
            registro_eventos()
        elif op == "9":
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
                    print(menu_admin())
                    return
            else:
                print("Usuario no encontrado.")
            
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")
inicio()

