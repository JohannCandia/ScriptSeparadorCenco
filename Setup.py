from cx_Freeze import Executable , setup
# Configuración
setup(
    name="Hola",
    version="1.0",
    description="Descripción de tu aplicación",
    executables=[Executable("Script.py")]
)
