from database import Base
from sqlalchemy import Column, Integer, String

class Libro(Base):
    
    __tablename__ = "libros"

    isbn = Column(String, primary_key=True)
    titulo = Column(String)
    autor = Column(String)
    editorial = Column(String)
    genero = Column(String)
    cantidad = Column(Integer)
    cantidad_disponible = Column(Integer)

    def __str__(self):
        return f"Libro: {self.isbn} - Título: {self.titulo} - Autor: {self.autor} - Editorial: {self.editorial} - Genero: {self.genero} - {self.cantidad_disponible} disponibles"
