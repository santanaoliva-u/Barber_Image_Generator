import os
import random
import subprocess

# Configuración de rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONDOS_DIR = os.path.join(BASE_DIR, "../fondos")
IMAGENES_DIR = os.path.join(BASE_DIR, "../img")
FUENTES_DIR = os.path.join(BASE_DIR, "../fuentes")
OUTPUT_DIR = os.path.join(BASE_DIR, "../output")
FUENTE = os.path.join(FUENTES_DIR, "ZuumeRough-Bold.ttf")

# Títulos para las imágenes
titulos = [
    "¡Transforma tu estilo con nosotros!",
    "¡Tu look perfecto está aquí!",
    "¡Renueva tu imagen hoy!",
    "¡El cuidado masculino que mereces!",
    "¡Estilo y elegancia garantizados!",
]

# Crear la carpeta de salida si no existe
os.makedirs(OUTPUT_DIR, exist_ok=True)

def seleccionar_archivo_aleatorio(carpeta):
    """Selecciona un archivo aleatorio de una carpeta."""
    archivos = [f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))]
    return os.path.join(carpeta, random.choice(archivos)) if archivos else None

def generar_imagen():
    """Genera una imagen combinando fondo, título e imagen central."""
    # Seleccionar fondo, imagen central y título
    fondo = seleccionar_archivo_aleatorio(FONDOS_DIR)
    imagen_central = seleccionar_archivo_aleatorio(IMAGENES_DIR)
    titulo = random.choice(titulos)

    if not fondo or not imagen_central:
        print("Error: Asegúrate de que las carpetas 'fondos' e 'img' contengan imágenes.")
        return

    # Configuración de dimensiones
    output_path = os.path.join(OUTPUT_DIR, f"output_{random.randint(1000, 9999)}.jpg")
    comando = [
        "magick", "convert",
        fondo,
        "-resize", "1080x1080^",
        "-gravity", "center",
        "-extent", "1080x1080",
        "(", imagen_central, "-resize", "600x600", "-gravity", "center", "-background", "none", "-extent", "600x600", ")",
        "-gravity", "center",
        "-composite",
        "-font", FUENTE,
        "-pointsize", "70",
        "-gravity", "north",
        "-fill", "white",
        "-annotate", "+0+50", titulo,
        output_path
    ]

    # Ejecutar el comando de ImageMagick
    subprocess.run(comando)
    print(f"Imagen generada: {output_path}")

if __name__ == "__main__":
    generar_imagen()

