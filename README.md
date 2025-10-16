# Conceptos — Fundamentos de Python

Colección de ejemplos, snippets y ejercicios usados en el curso de Fundamentos de Python. El objetivo es ofrecer piezas pequeñas y enfocadas para practicar el lenguaje: tipos y estructuras de datos, control de flujo, funciones, POO, E/S de archivos, llamadas a APIs, generadores/iteradores, y pequeños GUIs.

## Estructura

- `src/conceptos`: Módulos de ejemplo en formato de paquete instalable.
  - Básicos: `holamundo.py`, `tipos.py`, `cadenas.py`, `listas.py`, `tuplas.py`, `sets.py`, `diccionarios.py`.
  - Control de flujo y funciones: `condicionales.py`, `try_except.py`, `funciones.py`, `lambdas.py`, `decoradores.py`, `iteradores.py`, `generador_multiples_valores.py`.
  - Utilidades y demos: `archivos.py`, `mensajes.py`, `mensajes_colores.py`, `matematicas.py`, `round.py`, `switch.py`, `fechas.py`.
  - Integraciones: `api_access.py`, `omdb_demo.py`, `demo_requests.py`.
  - GUI (ejemplos simples): `gui.py`, `gui_hello_world.py`, `gui_list_dir.py`.
  - POO: carpeta `poo/` con clases y ejemplos (`coche.py`, `persona.py`, `factura.py`, `vehiculo.py`, `uso_termometro.py`, etc.).
  - Validación de datos: `pydantic/ejemplo_pydantic.py`.
- `Ejercicios`: Scripts autocontenidos para practicar (condicionales, listas/tuplas, generadores, POO, persistencia, E/S de archivos, etc.). Se pueden ejecutar individualmente.
- `test`: Pruebas básicas con `unittest` (por ejemplo, `test/conceptos/test_main.py`).
- `setup.py` y `src/`: Permiten instalar el paquete `conceptos` en editable para importar y ejecutar ejemplos como módulo.
- `environment.yml` / `requirements.txt`: Definición de entorno (mínimo, centrado en estándar de Python).

## Requisitos

- Python 3.10+ (recomendado 3.10 según `environment.yml`).
- Opcional: Conda/Mamba para gestionar el entorno, o `venv` con `pip`.

## Puesta en marcha (despliegue local)

Puedes trabajar de dos formas: instalando dependencias con Conda o usando `venv` + `pip`.

### Opción A: Conda/Mamba

```bash
cd Conceptos
conda env create -f environment.yml  # o: mamba env create -f environment.yml
conda activate conceptos
pip install -e .
```

### Opción B: venv + pip

```bash
cd Conceptos
python -m venv .venv
# Windows PowerShell
. .venv/Scripts/Activate.ps1
# macOS/Linux
source .venv/bin/activate

pip install -e .
# (opcional) pip install -r requirements.txt
```

Instalar en modo editable (`-e .`) facilita importar `conceptos` y utilizar los entry points definidos en `setup.py` (p. ej. `saludar`).

## Cómo ejecutar

- Ejecutar un módulo del paquete (tras instalar en editable):
  - `python -m conceptos.holamundo`
  - `python -m conceptos.saludar`
  - `python -m conceptos.cadenas`

- Ejecutar un ejercicio (desde la carpeta `Conceptos` o usando rutas relativas):
  - `python Ejercicios/Ejercicio0.py`
  - `python Ejercicios/ejercicio_condicionales_con_enumerate.py`
  - `python Ejercicios/peliculas_persistencia.py`

- Pruebas (unittest):
  - `python -m unittest discover -s test`

## Notas

- `requirements.txt` está vacío por diseño: los ejemplos usan principalmente la librería estándar. Algunos módulos de demostración (API/GUI) pueden requerir paquetes adicionales; añádelos según necesidades y reinstala.
- Los GUIs están pensados como demos simples (tkinter). Ejecuta cada script de forma independiente.
- Si vas a importar desde `src/` sin instalar el paquete, recuerda configurar `PYTHONPATH` o usar `pip install -e .`.

## Siguientes pasos sugeridos

- Completar `requirements.txt` con dependencias puntuales si usas módulos externos en tus ejercicios.
- Añadir más pruebas en `test/` para cubrir snippets clave.
- Explorar y extender los ejemplos de POO en `src/conceptos/poo`.

¡Feliz aprendizaje y práctica con Python!
