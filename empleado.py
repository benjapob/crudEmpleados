from persona import Persona


class Empleado(Persona):
    def __init__(self, rut, clave, nombre, cargo, depto):
        super().__init__(rut, clave, nombre, cargo)
        self.__listaEmpleado = []
        self.__depto = depto

    def __str__(self):
        return f"{super().__str__()} \nDepartamento: {self.__depto}"

    def setDepto(self, depto):
        self.__depto = depto

    def getDepto(self):
        return self.__depto

    def getListaEmpleado(self):
        if len(self.__listaEmpleado) != 0:
            return self.__listaEmpleado
        else:
            print("No hay empleados ingresados")

    def mostrarTodos(self):
        if len(self.__listaEmpleado) != 0:
            for a in self.__listaEmpleado:
                print(a)
        else:
            print("No hay empleados ingresados")

    def addEmpleado(self, rut, clave, nombre, cargo, depto):
        e = Empleado(rut, clave, nombre, cargo, depto)
        if e not in self.__listaEmpleado:
            self.__listaEmpleado.append(e)
            print("Empleado ingresado correctamente")
        else:
            print("Empleado ya existe")

    def buscarEmpleado(self, rut):
        if len(self.__listaEmpleado) != 0:
            for a in self.__listaEmpleado:
                if rut == a.getRut():
                    return a
                else:
                    return False
        else:
            print("No hay empleados ingresados")
            return False

    def subEmpleado(self, rut):
        e = self.buscarEmpleado(rut)
        if e is not False:
            self.__listaEmpleado.remove(e)
            print("Empleado eliminado exitosamente!")
        else:
            print("Empleado no encontrado")

    def modificarEmpleado(self, clave, opcion, rut):
        e = self.buscarEmpleado(rut)
        if e is not False:
            if opcion == 1:
                e.setClave(clave)
                print("Clave modificada exitosamente!")
            elif opcion == 2:
                e.setNombre(clave)
                print("Nombre modificado exitosamente!")
            elif opcion == 3:
                e.setCargo(clave)
                print("Cargo modificado exitosamente!")
            else:
                print("Opcion no válida")
        else:
            print("Empleado no encontrado")


# variable para usar métodos
emp = Empleado("", "", "", "", "")
