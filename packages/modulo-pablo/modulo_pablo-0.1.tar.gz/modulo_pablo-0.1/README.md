# Módulo-Pablo

**Módulo Pablo** es un paquete de Python que incluye funcionalidades de ejemplo para saludar, despedir, y mostrar imágenes aleatorias desde una URL en función del sistema operativo en el que se ejecute.

## Características

- Saludos y despedidas personalizadas que incluyen el nombre del módulo.
- Descarga y visualización automática de imágenes desde una URL proporcionada.
- Compatible con sistemas operativos Windows, macOS y Linux para abrir la imagen descargada.

## Instalación

Para instalar el módulo desde PyPI:

```bash
pip install modulo-pablo
```

### Instalación desde GitHub

Si prefieres instalar el módulo directamente desde el repositorio de GitHub:

```bash
pip install git+https://github.com/Duz-Dev/modulo-pablo.git
```

## Uso

A continuación, se presentan algunos ejemplos de uso del módulo `pablo`:

### Saludo

```python
import modulo_pablo

# Saludo personalizado
nombre = "Juan"
saludo = modulo_pablo.saludar(nombre)
print(saludo)
```

### Despedida

```python
import modulo_pablo

# Despedida personalizada
nombre = "Juan"
despedida = modulo_pablo.despedir(nombre)
print(despedida)
```

### Mostrar Imagen Aleatoria

```python
import modulo_pablo

# Mostrar una imagen desde una URL (se abrirá automáticamente con el visor por defecto)
modulo_pablo.img_random("https://i.postimg.cc/YCWcC2zN/wallhaven-j5mj3w-1920x1080.png")
```

El método `img_random` descarga la imagen desde la URL proporcionada y la muestra con el visor predeterminado según el sistema operativo (Windows, macOS o Linux).

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza los cambios en tu rama.
4. Haz commit de tus cambios (`git commit -am 'Añadir nueva funcionalidad'`).
5. Sube los cambios a tu fork.
6. Envía un Pull Request detallando tus cambios.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

- **Autor**: Ruben Chavez
- **Correo**: <pablo.dev.academy@gmail.com>
- **Repositorio en GitHub**: [https://github.com/Duz-Dev/modulo-pablo](https://github.com/Duz-Dev/modulo-pablo)
