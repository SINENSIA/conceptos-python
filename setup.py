from setuptools import setup, find_packages

setup(
    name='conceptos',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'indentacion = conceptos.identacion:indentacion',
            'saludar = conceptos.saludar:main',
        ],
    },
    # ... (otros argumentos de setup)
)