class AccessStrategy:
    """Clase base para estrategias de acceso."""
    def has_access(self, user_role):
        raise NotImplementedError

class AdminAccess(AccessStrategy):
    """Acceso para administradores."""
    def has_access(self, user_role):
        return user_role == "admin"

class EditorAccess(AccessStrategy):
    """Acceso para editores."""
    def has_access(self, user_role):
        return user_role in ["admin", "editor"]

class VisitorAccess(AccessStrategy):
    """Acceso para visitantes."""
    def has_access(self, user_role):
        return user_role in ["admin", "editor", "visitor"]

class AccessControl:
    """Clase que gestiona el acceso según la estrategia aplicada."""
    def __init__(self, strategy: AccessStrategy):
        self.strategy = strategy

    def check_access(self, user_role):
        return self.strategy.has_access(user_role)

# Ejemplo de uso
admin = AccessControl(AdminAccess())
editor = AccessControl(EditorAccess())
visitor = AccessControl(VisitorAccess())

print(admin.check_access("editor"))  # False
print(editor.check_access("editor"))  # True
print(visitor.check_access("visitor"))  # True