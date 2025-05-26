
# Producto
class Reporte:
    def __init__(self):
        self.partes = []

    def agregar_parte(self, parte):
        self.partes.append(parte)

    def mostrar(self):
        print("Reporte generado:")
        for parte in self.partes:
            print(f"- {parte}")

# Builder
class ReporteBuilder:
    def __init__(self):
        self.reporte = Reporte()

    def agregar_titulo(self):
        self.reporte.agregar_parte("Título del Reporte")

    def agregar_tabla(self):
        self.reporte.agregar_parte("Tabla de Datos")

    def agregar_grafico(self):
        self.reporte.agregar_parte("Gráfico de Barras")

    def agregar_resumen(self):
        self.reporte.agregar_parte("Resumen Ejecutivo")

    def obtener_reporte(self):
        return self.reporte

# Director
class Director:
    def __init__(self, builder: ReporteBuilder):
        self.builder = builder

    def construir_reporte_completo(self):
        self.builder.agregar_titulo()
        self.builder.agregar_tabla()
        self.builder.agregar_grafico()
        self.builder.agregar_resumen()

# Uso
builder = ReporteBuilder()
director = Director(builder)
director.construir_reporte_completo()
reporte = builder.obtener_reporte()
reporte.mostrar()
