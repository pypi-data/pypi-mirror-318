from setuptools import setup

# Asegúrate de abrir el README con la codificación UTF-8
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='modulo_pablo',
    packages=['modulo_pablo'],  # este debe ser el mismo que el nombre anterior
    version='0.1.3',
    description='Paquete creado con fines educativos. Mas informacion: github.com/Duz-Dev',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ruben Chavez',
    author_email='pablo.dev.academy@gmail.com',
    # use the URL to the github repo
    url='https://github.com/Duz-Dev/modulo-pablo',
    download_url='https://github.com/Duz-Dev/modulo-pablo/tarball/0.1.3',
    keywords=['testing', 'logging', 'example'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    install_requires=[
        "pillow",
        "requests", 
    ],
    include_package_data=True
)