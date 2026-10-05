from modelo.estudiante import Estudiante


class SaludoService:
    def __init__(self) -> None:
        self._estudiante: Estudiante | None = None

    def registrar(self, nombre: str, edad: str, hora: str) -> Estudiante:
        self._estudiante = Estudiante.crear(nombre, edad, hora)
        return self._estudiante

    def tiene_datos(self) -> bool:
        return self._estudiante is not None

    def saludar(self) -> str:
        if self._estudiante is None:
            raise ValueError(
                "Debe registrar nombre, edad y hora antes de solicitar el saludo."
            )
        e = self._estudiante
        return (
            f"¡Hola, {e.nombre}! Tienes {e.edad} años. Son las {e.hora}. "
            "¡Que tengas un excelente día de estudio!"
        )
