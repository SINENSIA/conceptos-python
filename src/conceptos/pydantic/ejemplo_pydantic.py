from pydantic import BaseModel
from pydantic import ValidationError
from datetime import datetime
# dfinir modelo


class Usuario(BaseModel):
    nombre: str
    edad: int
    email: str
    direccion: str = "Ninguna"
    telefono: int | None = None
    created_at: datetime = datetime.today()


# validacion
datos = {
    "nombre": "Carlos",
    "edad": 30,
    "email": "carlos@example.com"
}

usuario = Usuario(**datos)
print(usuario)

try:
    usuario2 = Usuario(nombre="Carlos", edad="30",
                       email="carlos@example.com", telefono="4343", created_at=datetime(1990, 5, 20, 0, 0))
except ValidationError as e:
    print(e)

print(usuario2)
