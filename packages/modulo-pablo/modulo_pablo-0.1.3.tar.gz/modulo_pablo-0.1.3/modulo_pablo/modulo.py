# modulo_pablo.py

# URL de la imagen por default
_url = "https://i.postimg.cc/YCWcC2zN/wallhaven-j5mj3w-1920x1080.png"

def saludar(name: str) -> str:
    """
    Función para saludar al usuario.

    Argumentos:
    name -- nombre de la persona a saludar

    Retorna:
    Un mensaje de saludo.
    """
    return f"Hola {name}, te brindo un saludo desde el modulo con el nombre '{__name__}'"

def img_random(imagen_url: str = _url) -> None:
    """
    Función para descargar y abrir una imagen desde una URL.

    Argumentos:
    imagen_url -- URL de la imagen a mostrar (opcional)

    Este método descarga la imagen, la guarda localmente y la abre 
    con el visor predeterminado del sistema operativo.
    """
    # Importar las librerías dentro de la función para evitar exponerlas
    import requests
    import os
    import platform
    import subprocess
    from PIL import Image
    from io import BytesIO

    # Descargar la imagen desde la URL
    try:
        # Puedes establecer un timeout explícito, como 10 segundos, para evitar que la espera sea indefinida
        respuesta = requests.get(imagen_url, timeout=6)  # Timeout de 10 segundos
        
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
            
    # Capturar errores específicos de timeout en requests
    except requests.exceptions.Timeout as e:
        print("Se excedió el tiempo de la petición:", e)
    # Capturar cualquier otro error relacionado con requests
    except requests.exceptions.RequestException as e:
        print("Ocurrió un error con la petición:", e)
    # Capturar cualquier otro error inesperado
    except Exception as e:
        print("Ocurrió un error inesperado:", e)
