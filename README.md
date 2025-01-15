# Generador de Imágenes Automatizado
![Demostracion 1](/recursos/1.png) 
Este proyecto permite generar imágenes dinámicas combinando fondos, imágenes centrales, texto y filtros avanzados. Está dividido en dos módulos principales:

- **main.py**: Diseñado para generar una sola imagen interactiva. Es ideal para pruebas y ajustes.
- **gen.py**: Permite la generación masiva de imágenes con configuraciones personalizables desde la línea de comandos.

## Características principales

- **Combinación de imágenes**: Une fondos con imágenes centrales, texto y detalles adicionales.
- **Filtros avanzados**: Aplica efectos como verde, azul, café y negro con niveles de intensidad configurables.
- **Generación masiva**: Soporte para producir varias imágenes en un solo comando.
- **Configuración fácil**: Uso simple de argumentos para personalizar el proceso.

---

## Requisitos

1. **Python**: Versión 3.8 o superior.
2. **Dependencias de Python**: Gestionadas a través de `requirements.txt`.
3. **Pillow**: Librería para procesamiento de imágenes.
4. **ImageMagick**: Herramienta opcional para manipulación de imágenes (si aplica).

---

## Instalación

1. **Clonar el repositorio**:

```bash
$ git clone https://github.com/usuario/Barber_Image_Generator.git
$ cd Barber_Image_Generator
```

2. **Crear y activar un entorno virtual**:

```bash
$ python3 -m venv env
$ source env/bin/activate
```

3. **Instalar dependencias**:

```bash
$ pip install -r requirements.txt
```

4. **Configurar las carpetas de recursos**:

Asegúrate de tener las carpetas y archivos necesarios en el repositorio:

- `fondos`: Imágenes de fondo (preferentemente cuadradas).
- `img`: Imágenes centrales (PNG transparente recomendado).
- `fuentes`: Archivos TTF para las fuentes tipográficas.
- `output`: Carpeta donde se guardarán las imágenes generadas.

---

## Uso de los módulos

### 1. **main.py**

Genera una sola imagen personalizada de manera interactiva. Ejecución:

```bash
$ python main.py
```

**Flujo de trabajo**:

1. Solicita elegir un filtro (verde, azul, café, negro o sin filtro).
2. Permite ajustar la intensidad del filtro (de 1 a 10).
3. Combina un fondo aleatorio con una imagen central y texto.
4. Genera un post con hashtags y detalles copiados al portapapeles.

### 2. **gen.py**

Este módulo permite generar múltiples imágenes de forma masiva con configuraciones personalizadas desde la línea de comandos.

**Ejemplos de uso**:

- **Generar 13 imágenes sin filtros**:

```bash
$ python gen.py -c 13
```

- **Generar 10 imágenes con filtro verde e intensidad 5**:

```bash
$ python gen.py -f verde -i 5 -c 10
```

- **Generar 5 imágenes con filtro café e intensidad máxima**:

```bash
$ python gen.py -f cafe -i 10 -c 5
```

**Argumentos**:

- `-c`: Cantidad de imágenes a generar (por defecto, 1).
- `-f`: Filtro a aplicar (`verde`, `azul`, `cafe`, `negro`, o ninguno).
- `-i`: Intensidad del filtro (1-10, por defecto 1).

---

## Explicación del código

### Estructura principal

- **main.py**:
  Diseñado para facilitar pruebas interactivas y ajustes de configuración de imágenes individuales.

- **gen.py**:
  
  Extiende las funcionalidades de `main.py` para procesar múltiples imágenes de manera eficiente y escalable.

### Funciones clave

1. **seleccionar_archivo_aleatorio**:
   Selecciona un archivo aleatorio de una carpeta especificada.

2. **aplicar_filtro_avanzado**:
   Aplica efectos visuales a los fondos con ajustes matemáticos para cada canal RGB.

3. **ajustar_brillo_contraste**:
   Ajusta los niveles de brillo y contraste para mejorar la calidad visual de las imágenes.

4. **limpiar_emojis**:
   Elimina emojis y caracteres no admitidos del texto para asegurar compatibilidad.

5. **generar_imagen**:
   Une todos los elementos visuales (fondos, imágenes centrales, textos) y guarda el resultado.

---

## Posibles mejoras

1. **Base de datos para gestión de textos**:
   Almacenar títulos, servicios y otros textos en un archivo JSON o base de datos SQLite.

2. **Selección de imágenes específicas**:
   Agregar opciones para elegir archivos específicos en lugar de seleccionar aleatoriamente.

3. **Soporte para formatos adicionales**:
   Ampliar compatibilidad con formatos como SVG y WebP.

4. **Interfaz gráfica**:
   Crear una GUI para usuarios menos técnicos.

5. **Integración con redes sociales**:
   Automatizar la publicación de las imágenes generadas en Instagram o Facebook.

---

## Créditos

Este proyecto fue desarrollado por **Jesús Uriel Santana Oliva**.

- **Ubicación**: 77724, Guadalupana, Playa del Carmen, México.
- **Correo**: santanabarberoprofesional@gmail.com
- **Redes Sociales**: [Instagram](https://instagram.com/santanaoliva_u)

---

**Repositorio del proyecto**:
[GitHub](https://github.com/santanaoliva-u/Barber_Image_Generator)


