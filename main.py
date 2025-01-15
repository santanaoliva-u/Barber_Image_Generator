import os
import random
import pyperclip
from PIL import Image, ImageDraw, ImageEnhance, ImageFont
import numpy as np
import math

# Configuración de rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONDOS_DIR = os.path.join(BASE_DIR, "fondos")
IMAGENES_DIR = os.path.join(BASE_DIR, "img")
FUENTES_DIR = os.path.join(BASE_DIR, "fuentes")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
FUENTE = os.path.join(FUENTES_DIR, "ZuumeRough-Bold.ttf")

# Crear la carpeta de salida si no existe
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Títulos y texto
TITULOS = [
    "¡Transforma tu estilo con nosotros!",
    "¡Tu look perfecto está aquí!",
    "¡Renueva tu imagen hoy!",
    "¡El cuidado masculino que mereces!",
    "¡Estilo y elegancia garantizados!",
]

SERVICIOS = [
    "✔️ Cortes modernos y clásicos.",
    "✔️ Diseño y perfilado de barba.",
    "✔️ Tratamientos premium.",
    "✔️ Cortes personalizados para todos los estilos.",
    "✔️ Diseño único para cada cliente.",
    "✔️ Estilizado y acabado con productos de alta calidad.",
    "✔️ Asesoría en estilo personal.",
    "✔️ Afeitado profesional con navaja.",
]

INFO_EXTRA = (
    " Ubicación: 77724, Guadalupana, Playa del Carmen, México\n"
    " Sitio Web: https://jesus-uriel-santana-oliva.gitbook.io/barbero-profesional" 
    " Correo: santanabarberoprofesional@gmail.com\n"
    " 984 187 0157\n"
    "@santanaoliva_u"
    "               "
)

INFO_EXTRA_IMG = (
    " Ubicación: 77724, Guadalupana, Playa del Carmen, México\n"
    " 984 187 0157\n"
    "@santanaoliva_u"
)

HASHTAGS = (
    "#BarberoPlayaDelCarmen #CortesDeCabello #EstiloProfesional #BarberShopPlaya "
    "#CortesMasculinos #EstiloPersonal #LookPerfecto #CuidadoMasculino"
)

# Selección aleatoria de archivos
def seleccionar_archivo_aleatorio(carpeta):
    archivos = [f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))]
    return os.path.join(carpeta, random.choice(archivos)) if archivos else None

# Aplicar filtro avanzado
def aplicar_filtro_avanzado(imagen, filtro, intensidad):
    np_img = np.array(imagen, dtype=np.float32) / 255.0
    
    # Filtro matemático avanzado basado en transformación de canales
    if filtro == "verde":
        np_img[:, :, 1] = np.clip(np_img[:, :, 1] + intensidad * 0.1, 0, 1)  # Modificar canal verde
    elif filtro == "azul":
        np_img[:, :, 2] = np.clip(np_img[:, :, 2] + intensidad * 0.1, 0, 1)  # Modificar canal azul
    elif filtro == "cafe":
        r, g, b = np_img[:, :, 0], np_img[:, :, 1], np_img[:, :, 2]
        promedio = (r + g + b) / 3
        np_img[:, :, :] = np.clip(promedio[:, :, None] * (1 + intensidad * 0.05), 0, 1)  # Aplicar tono cálido
    elif filtro == "negro":
        gris = np.mean(np_img, axis=2)  # Conversión a escala de grises
        np_img[:, :, :] = np.clip(gris[:, :, None] * (1 - intensidad * 0.05), 0, 1)
    
    # Normalización y restauración de la imagen
    np_img = np.clip(np_img, 0, 1)
    return Image.fromarray((np_img * 255).astype(np.uint8))

# Eliminar emojis del texto
def limpiar_emojis(texto):
    return ''.join(c for c in texto if c.isalnum() or c.isspace() or c in "¡!¿?.,:")

# Función matemática avanzada para ajuste de brillo y contraste
def ajustar_brillo_contraste(imagen, brillo=1.0, contraste=1.0):
    np_img = np.array(imagen, dtype=np.float32) / 255.0

    # Brillo: simple suma multiplicada
    np_img *= brillo

    # Contraste: fórmula de contraste
    promedio = np.mean(np_img, axis=(0, 1), keepdims=True)
    np_img = np.clip((np_img - promedio) * contraste + promedio, 0, 1)

    return Image.fromarray((np_img * 255).astype(np.uint8))

# Generar imagen
def generar_imagen():
    fondo = seleccionar_archivo_aleatorio(FONDOS_DIR)
    imagen_central = seleccionar_archivo_aleatorio(IMAGENES_DIR)
    titulo = random.choice(TITULOS)

    if not fondo or not imagen_central:
        print("Error: Asegúrate de que las carpetas 'fondos' e 'img' contengan imágenes.")
        return

    # Selección de filtro
    while True:
        try:
            print("Selecciona un filtro:")
            print("1. Verde")
            print("2. Azul")
            print("3. Café")
            print("4. Negro")
            print("5. Sin filtro")
            opcion_filtro = int(input("Ingresa el número del filtro: "))
            if 1 <= opcion_filtro <= 5:
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    intensidad = 0
    if opcion_filtro != 5:  # Si no es "Sin filtro"
        while True:
            try:
                intensidad = int(input("Ingresa la intensidad del filtro (1-10): "))
                if 1 <= intensidad <= 10:
                    break
            except ValueError:
                print("Por favor, ingresa un número válido.")

    filtros = {1: "verde", 2: "azul", 3: "cafe", 4: "negro", 5: None}
    filtro_seleccionado = filtros.get(opcion_filtro)

    # Abrir imágenes
    fondo_img = Image.open(fondo).resize((1080, 1080)).convert("RGB")
    imagen_central_img = Image.open(imagen_central).resize((600, 600)).convert("RGBA")

    # Aplicar filtro al fondo si es necesario
    if filtro_seleccionado:
        fondo_img = aplicar_filtro_avanzado(fondo_img, filtro_seleccionado, intensidad)

    # Ajuste de brillo y contraste (matemáticamente avanzado)
    fondo_img = ajustar_brillo_contraste(fondo_img, brillo=1.1, contraste=1.2)

    # Combinar imágenes
    fondo_img.paste(imagen_central_img, (240, 240), imagen_central_img)

    # Dibujar texto
    draw = ImageDraw.Draw(fondo_img)
    font_titulo = ImageFont.truetype(FUENTE, 70)
    font_info = ImageFont.truetype(FUENTE, 40)

    # Agregar título (sin emojis)
    titulo_limpio = limpiar_emojis(titulo)
    text_bbox = draw.textbbox((0, 0), titulo_limpio, font=font_titulo)
    text_width = text_bbox[2] - text_bbox[0]
    draw.text(((1080 - text_width) / 2, 50), titulo_limpio, font=font_titulo, fill="white")

    # Agregar información adicional
    draw.text((50, 950), INFO_EXTRA_IMG, font=font_info, fill="white")

    # Guardar imagen
    output_path = os.path.join(OUTPUT_DIR, f"output_{random.randint(1000, 9999)}.jpg")
    fondo_img.save(output_path)
    print(f"Imagen generada: {output_path}")

    # Generar post
    servicios_texto = "\n".join(SERVICIOS)
    post = (
        f"{titulo}\n\n"
        f"{servicios_texto}\n\n"
        f"{INFO_EXTRA}\n\n"
        f"{HASHTAGS}"
    )

    pyperclip.copy(post)
    print("Post generado y copiado al portapapeles:\n")
    print(post)

if __name__ == "__main__":
    generar_imagen()

