import requests
import os
import platform
import subprocess
from PIL import Image
from io import BytesIO

# URL de la imagen por default
# url = "https://i.postimg.cc/906xxjJJ/rei-rei-ayanami.gif"
url = "https://i.postimg.cc/YCWcC2zN/wallhaven-j5mj3w-1920x1080.png"

def saludar(name: str)-> str:
    return f"Hola {name}, te brindo un saludo desde el modulo con el nombre '{__name__}'"

def img_random(imagen_url: str = url) -> None:
    # Descargar la imagen desde la URL
    respuesta = requests.get(imagen_url)
    
    # Usar Pillow para abrir la imagen desde los bytes
    imagen = Image.open(BytesIO(respuesta.content))

    # Obtener el formato de la imagen (gif, png, etc.)
    formato = imagen.format.lower()
    nombre_archivo = f"imagen.{formato}"

    # Guardar la imagen con el formato adecuado
    with open(nombre_archivo, "wb") as f:
        f.write(respuesta.content)

    # Detectar el sistema operativo
    sistema = platform.system()

    # Abrir la imagen con el visor predeterminado según el sistema
    if sistema == "Windows":
        os.startfile(nombre_archivo)  # Windows
    elif sistema == "Darwin":  # macOS
        subprocess.run(["open", nombre_archivo])
    elif sistema == "Linux":
        subprocess.run(["xdg-open", nombre_archivo])
    else:
        print("Sistema operativo no soportado para abrir la imagen automáticamente.")

