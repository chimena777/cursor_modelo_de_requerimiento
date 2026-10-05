import re
from dataclasses import dataclass


@dataclass
class Estudiante:
    nombre: str
    edad: int
    hora: str

    @staticmethod
    def validar_nombre(nombre: str) -> str:
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        return nombre

    @staticmethod
    def validar_edad(edad_str: str) -> int:
        try:
            edad = int(edad_str.strip())
        except ValueError:
            raise ValueError("La edad debe ser un número entero.")
        if edad < 1 or edad > 120:
            raise ValueError("La edad debe estar entre 1 y 120.")
        return edad

    @staticmethod
    def validar_hora(hora: str) -> str:
        hora = hora.strip()
        if not re.fullmatch(r"([01]?\d|2[0-3]):[0-5]\d", hora):
            raise ValueError("La hora debe tener formato HH:MM (24 horas).")
        partes = hora.split(":")
        return f"{int(partes[0]):02d}:{partes[1]}"

    @classmethod
    def crear(cls, nombre: str, edad_str: str, hora: str) -> "Estudiante":
        return cls(
            nombre=cls.validar_nombre(nombre),
            edad=cls.validar_edad(edad_str),
            hora=cls.validar_hora(hora),
        )
