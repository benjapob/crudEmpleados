class Persona:
    def __init__(self, rut, clave, nombre, cargo):
        self.__rut = rut
        self.__clave = clave
        self.__nombre = nombre
        self.__cargo = cargo

    def __str__(self):
        return f"Rut:{self.__rut} \nNombre:{self.__nombre} \nCargo:{self.__cargo} "

    def setRut(self, rut):
        self.__rut = rut

    def setClave(self, clave):
        self.__clave = clave

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setCargo(self, cargo):
        self.__cargo = cargo

    def getRut(self):
        return self.__rut

    def getClave(self):
        return self.__clave

    def getNombre(self):
        return self.__nombre

    def getCargo(self):
        return self.__cargo
