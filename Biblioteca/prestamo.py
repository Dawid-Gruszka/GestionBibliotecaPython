from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from datetime import datetime
class Prestamo(Base):
    
    __tablename__ = "prestamos"

    id = Column(Integer, primary_key=True)
    socio_dni = Column(String, ForeignKey("socios.dni"))
    libro_isbn = Column(String, ForeignKey("libros.isbn"))
    fecha_prestamo = Column(DateTime, default=datetime.now())
    fecha_devolucion = Column(DateTime)
    devuelto = Column(Boolean, default=False)

    def __str__(self):
        return f"Prestamo: {self.socio_dni} - ISBN:  {self.libro_isbn} - Fecha Prestamo: {self.fecha_prestamo} - Fecha Devolucion {self.fecha_devolucion} - Devuelto: {self.devuelto}"
