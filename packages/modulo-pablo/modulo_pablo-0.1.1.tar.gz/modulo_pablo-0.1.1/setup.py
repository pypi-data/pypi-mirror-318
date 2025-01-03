from setuptools import setup

readme = open("./README.md", "r")


setup(
    name='modulo_pablo',
    packages=['modulo_pablo'],  # this must be the same as the name above
    version='0.1.1',
    description='Esta es la descripcion de mi paquete',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='Ruben Chavez',
    author_email='pablo.dev.academy@gmail.com',
    # use the URL to the github repo
    url='https://github.com/Duz-Dev/modulo-pablo',
    download_url='https://github.com/Duz-Dev/modulo-pablo/tarball/0.1',
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