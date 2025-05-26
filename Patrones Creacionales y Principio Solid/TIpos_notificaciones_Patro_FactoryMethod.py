
# Clase abstracta que define la interfaz común para todas las notificaciones
from abc import ABC, abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

# Clases concretas que implementan la interfaz Notificacion
class Email(Notificacion):
    def enviar(self, mensaje):
        print(f"Enviando Email: {mensaje}")

class SMS(Notificacion):
    def enviar(self, mensaje):
        print(f"Enviando SMS: {mensaje}")

class Push(Notificacion):
    def enviar(self, mensaje):
        print(f"Enviando Notificación Push: {mensaje}")

# Clase abstracta que define la interfaz para crear notificaciones
class NotificacionFactory(ABC):
    @abstractmethod
    def crear_notificacion(self) -> Notificacion:
        pass

# Fábricas concretas que crean instancias de cada tipo de notificación
class EmailFactory(NotificacionFactory):
    def crear_notificacion(self):
        return Email()

class SMSFactory(NotificacionFactory):
    def crear_notificacion(self):
        return SMS()

class PushFactory(NotificacionFactory):
    def crear_notificacion(self):
        return Push()

# Función que usa la fábrica para crear y enviar una notificación
def enviar_alerta(factory: NotificacionFactory, mensaje: str):
    notificacion = factory.crear_notificacion()
    notificacion.enviar(mensaje)

# Ejemplo de uso
enviar_alerta(EmailFactory(), "¡Tienes un nuevo mensaje!")
enviar_alerta(SMSFactory(), "Código de verificación: 1234")
