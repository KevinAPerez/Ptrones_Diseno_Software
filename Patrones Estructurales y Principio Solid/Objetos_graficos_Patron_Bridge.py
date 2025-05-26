
from abc import ABC, abstractmethod

# Implementación: interfaz para renderizado
class Renderizador(ABC):
    @abstractmethod
    def renderizar(self, nombre_objeto: str):
        pass

# Implementaciones concretas
class RenderizadorPantalla(Renderizador):
    def renderizar(self, nombre_objeto: str):
        print(f"Renderizando '{nombre_objeto}' en pantalla.")

class RenderizadorImpresion(Renderizador):
    def renderizar(self, nombre_objeto: str):
        print(f"Renderizando '{nombre_objeto}' para impresión.")

# Abstracción: objeto gráfico
class ObjetoGrafico(ABC):
    def __init__(self, renderizador: Renderizador):
        self.renderizador = renderizador

    @abstractmethod
    def dibujar(self):
        pass

# Abstracciones refinadas
class Imagen(ObjetoGrafico):
    def dibujar(self):
        self.renderizador.renderizar("Imagen")

class Texto(ObjetoGrafico):
    def dibujar(self):
        self.renderizador.renderizar("Texto")

# Uso del patrón Bridge
renderizador_pantalla = RenderizadorPantalla()
renderizador_impresion = RenderizadorImpresion()

imagen = Imagen(renderizador_pantalla)
texto = Texto(renderizador_impresion)

imagen.dibujar()  # Renderizando 'Imagen' en pantalla.
texto.dibujar()   # Renderizando 'Texto' para impresión.
