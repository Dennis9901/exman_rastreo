try:
    from examen_rastreo.wsgi import application
    print("¡Importación exitosa! La variable 'application' está disponible.")
except ModuleNotFoundError as e:
    print(f"Error de módulo no encontrado: {e}")
except AttributeError as e:
    print(f"Error de atributo: {e}")
except Exception as e:
    print(f"Otro error ocurrió: {e}")
