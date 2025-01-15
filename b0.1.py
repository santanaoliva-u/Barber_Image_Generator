import os
import random
import pyperclip
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

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
    "💈 ¡Transforma tu estilo con nosotros!",
    "🪒 ¡Tu look perfecto está aquí!",
    "💇‍♂️ ¡Renueva tu imagen hoy!",
    "🌟 ¡El cuidado masculino que mereces!",
    "🪒 ¡Estilo y elegancia garantizados!",
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
    "📍 Ubicación: 77724, Guadalupana, Playa del Carmen, México\n"
    "📧 Correo: santanabarberoprofesional@gmail.com\n"
    "📞 984 187 0157\n"
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

# Aplicar filtro
def aplicar_filtro(imagen, filtro, intensidad):
    if filtro == "verde":
        r, g, b = imagen.split()
        g = g.point(lambda i: i + intensidad * 10)
        return Image.merge("RGB", (r, g, b))
    elif filtro == "azul":
        r, g, b = imagen.split()
        b = b.point(lambda i: i + intensidad * 10)
        return Image.merge("RGB", (r, g, b))
    elif filtro == "cafe":
        enhancer = ImageEnhance.Color(imagen)
        return enhancer.enhance(0.5 + (intensidad * 0.1))
    elif filtro == "negro":
        return imagen.convert("L").point(lambda x: x * (intensidad / 10))
    else:
        return imagen

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
            opcion_filtro = int(input("Ingresa el número del filtro: "))
            if 1 <= opcion_filtro <= 4:
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    while True:
        try:
            intensidad = int(input("Ingresa la intensidad del filtro (1-10): "))
            if 1 <= intensidad <= 10:
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    filtros = {1: "verde", 2: "azul", 3: "cafe", 4: "negro"}
    filtro_seleccionado = filtros.get(opcion_filtro)

    # Abrir imágenes
    fondo_img = Image.open(fondo).resize((1080, 1080)).convert("RGB")
    imagen_central_img = Image.open(imagen_central).resize((600, 600)).convert("RGBA")

    # Aplicar filtro al fondo
    fondo_img = aplicar_filtro(fondo_img, filtro_seleccionado, intensidad)

    # Combinar imágenes
    fondo_img.paste(imagen_central_img, (240, 240), imagen_central_img)

    # Dibujar texto
    draw = ImageDraw.Draw(fondo_img)
    font_titulo = ImageFont.truetype(FUENTE, 70)
    font_info = ImageFont.truetype(FUENTE, 40)

    # Agregar título
    text_bbox = draw.textbbox((0, 0), titulo, font=font_titulo)
    text_width = text_bbox[2] - text_bbox[0]
    draw.text(((1080 - text_width) / 2, 50), titulo, font=font_titulo, fill="white")

    # Agregar información adicional
    draw.text((50, 1000), INFO_EXTRA, font=font_info, fill="white")

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





















































































































































