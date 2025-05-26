class Observer:
    """Clase base para observadores."""
    def update(self, event):
        raise NotImplementedError

class Process(Observer):
    """Proceso que reacciona a cambios en el sistema operativo."""
    def __init__(self, name):
        self.name = name

    def update(self, event):
        print(f"Proceso {self.name} recibió evento: {event}")

class SystemEventNotifier:
    """Notificador de eventos del sistema."""
    def __init__(self):
        self.observers = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self, event):
        for observer in self.observers:
            observer.update(event)

# Ejemplo de uso
notifier = SystemEventNotifier()
process1 = Process("Proceso1")
process2 = Process("Proceso2")

notifier.add_observer(process1)
notifier.add_observer(process2)

notifier.notify_observers("Recursos disponibles")
notifier.notify_observers("Carga elevada detectada")