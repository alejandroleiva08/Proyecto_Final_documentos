from pathlib import Path

from paquete.Manejo_datos import cargar_datos, mostrar_datos
from paquete.Usuarios import introducir_datos

BASE_DIR = Path(__file__).resolve().parent
RUTA_BASE_DATOS = BASE_DIR / "base_de_datos.json"

def main():
    base_datos: list = cargar_datos(RUTA_BASE_DATOS)
    if type(base_datos) == list:
        introducir_datos(RUTA_BASE_DATOS, base_datos)
        mostrar_datos(base_datos)

main()