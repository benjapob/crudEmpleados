from empleado import Empleado, emp
from administrador import Administrador, admin


def volver():
    input("Presione enter para volver al menú...\n")


def continuar():
    input("Presione enter para continuar...\n")


def validarInt(cadena):
    try:
        numero = int(input(f"Ingresar {cadena} (sólo números): "))
        if numero > 0:
            return numero
        else:
            print("Debe ingresar un número válido")
            return validarInt(cadena)
    except:
        print("Debe ingresar un número válido")
        return validarInt(cadena)


def validarFloat(cadena):
    try:
        numero = float(input(f"Ingresar {cadena} (sólo números): "))
        if numero > 0:
            return numero
        else:
            print("Debe ingresar un número válido")
            return validarFloat(cadena)
    except:
        print("Debe ingresar un número válido")
        return validarFloat(cadena)


def validarStr(cadena):
    try:
        string = input(f"Ingresar {cadena}: ")
        if len(string) > 0:
            return string
        else:
            print("El campo no puede estar vacío")
            return validarStr(cadena)
    except:
        print("El campo no puede estar vacío")
        return validarStr(cadena)


def menuPrincipal():
    print(
        """---Menú---
1. Administrador
2. Empleado
3. Ayuda
4. Salir
"""
    )

    try:
        opcion = int(input("Ingrese opción: "))
        if opcion >= 1 and opcion <= 4:
            return opcion
        else:
            print(f"Opción {opcion} no válida\n")
            volver()
            return menuPrincipal()
    except:
        print("Opción no válida")
        volver()
        return menuPrincipal()


def menuSecundario():
    print(
        """---Menú---
1. Ingresar Empleado
2. Eliminar Empleado
3. Modificar empleado
4. Buscar Empleado
5. Mostrar Empleados
6. Volver al Menú Principal
"""
    )

    try:
        opcion2 = int(input("Ingrese opción: "))
        if opcion2 >= 1 and opcion2 <= 6:
            return opcion2
        else:
            print(f"Opción {opcion2} no válida\n")
            volver()
            return menuSecundario()
    except:
        print("Opción no válida")
        volver()
        return menuSecundario()


def menuModificar():
    print(
        """---Menú---
1. Modifica clave
2. Modifica nombre
3. Modifica cargo
4. Volver al menú anterior
"""
    )

    try:
        opcion3 = int(input("Ingrese opción: "))
        if opcion3 >= 1 and opcion3 <= 4:
            return opcion3
        else:
            print(f"Opción {opcion3} no válida\n")
            volver()
            return menuModificar()
    except:
        print("Opción no válida")
        volver()
        return menuModificar()


while True:
    opcion = menuPrincipal()

    if opcion == 1:
        acc = admin.getAcceso(
            validarInt("contraseña 1"), validarStr("contraseña 2"), validarStr("rut")
        )
        while acc is not False:
            opcion2 = menuSecundario()
            if opcion2 == 1:
                emp.addEmpleado(
                    validarStr("rut"),
                    validarStr("clave"),
                    validarStr("nombre"),
                    validarStr("cargo"),
                    validarStr("departamento"),
                )
                volver()
            elif opcion2 == 2:
                emp.subEmpleado(validarStr("rut"))
                volver()
            elif opcion2 == 3:
                mod = validarStr("rut a modificar")
                ver = emp.buscarEmpleado(mod)
                while ver is not False:
                    opcion3 = menuModificar()
                    if opcion3 == 1:
                        emp.modificarEmpleado(validarStr("clave a modificar"), 1, mod)
                        volver()
                    elif opcion3 == 2:
                        emp.modificarEmpleado(validarStr("nombre a modificar"), 2, mod)
                        volver()
                    elif opcion3 == 3:
                        emp.modificarEmpleado(validarStr("nombre a modificar"), 3, mod)
                        volver()
                    elif opcion3 == 4:
                        print("Volviendo al menú anterior")
                        break
                continuar()
            elif opcion2 == 4:
                e = emp.buscarEmpleado(validarStr("rut"))
                if e is not False:
                    print(e)
                else:
                    print("Empleado no encontrado")
                volver()
            elif opcion2 == 5:
                emp.mostrarTodos()
                volver()
            elif opcion2 == 6:
                print("Volviendo al menú principal")
                break
        else:
            break
        continuar()
    elif opcion == 2:
        print("Eliga otra opción")
        volver()
    elif opcion == 3:
        print("Eliga otra opción")
        volver()
    elif opcion == 4:
        print("Saliendo...")
        break
