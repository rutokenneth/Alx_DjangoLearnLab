from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

    def ready(self):
        import relationship_app.models # Import signals from models.py
        # Alternatively, if you put signals in a separate signals.py:
        # import relationship_app.signals
