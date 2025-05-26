class Handler:
    """Clase base para manejadores de solicitudes."""
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle_request(self, request):
        if self.next_handler:
            return self.next_handler.handle_request(request)
        return f"Solicitud '{request}' no pudo ser atendida."

class Level1Support(Handler):
    """Manejador de solicitudes de nivel 1."""
    def handle_request(self, request):
        if request in ["consulta básica", "pregunta frecuente"]:
            return f"Nivel 1 resolviendo solicitud: {request}"
        return super().handle_request(request)

class Level2Support(Handler):
    """Manejador de solicitudes de nivel 2."""
    def handle_request(self, request):
        if request in ["problema técnico menor", "soporte de configuración"]:
            return f"Nivel 2 resolviendo solicitud: {request}"
        return super().handle_request(request)

class Level3Support(Handler):
    """Manejador de solicitudes de nivel 3."""
    def handle_request(self, request):
        if request in ["error crítico", "fallo del sistema"]:
            return f"Nivel 3 resolviendo solicitud: {request}"
        return super().handle_request(request)

# Configuración de la cadena de responsabilidad
handler_chain = Level1Support(Level2Support(Level3Support()))

# Ejemplo de uso
print(handler_chain.handle_request("fallo del sistema"))