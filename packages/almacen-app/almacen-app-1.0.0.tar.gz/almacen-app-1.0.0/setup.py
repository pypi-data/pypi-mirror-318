from setuptools import setup, find_packages

setup(
    name='almacen-app',                         # Nombre único en PyPI
    version='1.0.0',                            # Versión del paquete
    packages=find_packages(),                   # Detectar automáticamente los paquetes
    include_package_data=True,                  # Incluir datos adicionales especificados
    install_requires=[                          # Dependencias necesarias
        'PySide6',
    ],
    entry_points={
        'console_scripts': [
            'almacen-app=main:main',            # Comando que ejecutará tu aplicación
        ]
    },
    author='Adrian Gregorio Ortiz',
    author_email='adrian@example.com',
    description='Aplicación de gestión para almacenes',
    long_description=open('LEEME.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AdrianGOrtiz/almacen-app',  # Repositorio del proyecto
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',                    # Versión mínima de Python
)
