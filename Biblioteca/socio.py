from database import Base
from sqlalchemy import Column, String, Integer

class Socio(Base):
    
    __tablename__ = "socios"

    dni = Column(String, primary_key=True)
    nombre = Column(String)
    telefono = Column(String)
    correo = Column(String)
    libros_prestados = Column(String)
    prestamos = Column(Integer)

    def __str__(self):
        return f"Socio: {self.dni} - Nombre: {self.nombre} - Telefono: {self.telefono} - Correo: {self.correo} - Libros Prestados {self.libros_prestados}"