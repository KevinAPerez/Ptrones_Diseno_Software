
from abc import ABC, abstractmethod

# Componente base
class ElementoArchivo(ABC):
    @abstractmethod
    def mostrar(self, nivel=0):
        pass

# Hoja: archivo individual
class Archivo(ElementoArchivo):
    def __init__(self, nombre: str):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("  " * nivel + f"- Archivo: {self.nombre}")

# Compuesto: carpeta que puede contener archivos y otras carpetas
class Carpeta(ElementoArchivo):
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.elementos = []

    def agregar(self, elemento: ElementoArchivo):
        self.elementos.append(elemento)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"+ Carpeta: {self.nombre}")
        for elemento in self.elementos:
            elemento.mostrar(nivel + 1)

# Uso del patrón Composite
raiz = Carpeta("Documentos")
carpeta_proyectos = Carpeta("Proyectos")
archivo_cv = Archivo("CV.pdf")
archivo_codigo = Archivo("codigo.py")

carpeta_proyectos.agregar(archivo_codigo)
raiz.agregar(archivo_cv)
raiz.agregar(carpeta_proyectos)

raiz.mostrar()
