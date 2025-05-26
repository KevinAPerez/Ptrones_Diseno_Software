
# Clase Singleton para la configuración global de una aplicación
class Configuracion:
    # Variable de clase para almacenar la única instancia
    _instancia = None

    # Método especial __new__ para controlar la creación de la instancia
    def __new__(cls):
        # Si no existe una instancia, crearla
        if cls._instancia is None:
            cls._instancia = super(Configuracion, cls).__new__(cls)
            # Inicializar atributos de configuración
            cls._instancia.idioma = "es"
            cls._instancia.tema = "oscuro"
        # Retornar la única instancia
        return cls._instancia

# Uso del patrón Singleton
config1 = Configuracion()
config2 = Configuracion()

# Cambiar el tema de la configuración usando una instancia
config1.tema = "claro"

# Verificar que el cambio se refleja en la otra instancia
print(config2.tema)  # Salida: claro (misma instancia)
print(config1 is config2)  # True (ambas referencias apuntan a la misma instancia)
