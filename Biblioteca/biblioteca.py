from Biblioteca.libro import Libro
from Biblioteca.socio import Socio
from Biblioteca.prestamo import Prestamo
from datetime import datetime
from database import SessionLocal

class biblioteca:

    def __init__(self):
        self.DB = SessionLocal()
    
    def alta_socio(self, dni, nombre, telefono, correo):
        if self.buscar_socio(dni):
            return False
        else:
            socio = Socio(dni=dni, nombre=nombre, telefono=telefono, correo=correo, prestamos=0)
            self.DB.add(socio)
            self.DB.commit()
            return True
    
    def baja_socio(self, dni):
        socio = self.buscar_socio(dni)
        if socio:
            if socio.prestamos == 0:
                self.DB.delete(socio)
                self.DB.commit()
                return True
            else:
                return False
        else:
            return False
    
    def alta_libro(self, isbn, titulo, autor, editorial, genero , cantidad):
        if self.buscar_libro(isbn):
            return False
        else:
            libro = Libro(isbn=isbn, titulo=titulo, autor=autor, editorial=editorial, genero=genero, cantidad=cantidad, cantidad_disponible=cantidad)
            self.DB.add(libro)
            self.DB.commit()
            return True
    
    def baja_libro(self, isbn):
        libro = self.buscar_libro(isbn)
        if libro:
            if libro.cantidad == libro.cantidad_disponible:
                self.DB.delete(libro)
                self.DB.commit()
                return True
            else:
                return False
        else:
            return False
    
    def prestamo_libro(self, dni, isbn):
        socio = self.buscar_socio(dni)
        libro = self.buscar_libro(isbn)
        if socio and libro:
            if libro.cantidad_disponible > 0:
                prestamo = Prestamo(socio_dni=dni, libro_isbn=isbn)
                libro.cantidad_disponible -= 1
                socio.prestamos += 1
                self.DB.add(prestamo)
                self.DB.commit()
                return True
            else:
                return False
        else:
            return False
        
    def devolucion_libro(self, dni, isbn):
        socio = self.buscar_socio(dni)
        libro = self.buscar_libro(isbn)
        if socio and libro:
            prestamo = self.DB.query(Prestamo).filter(Prestamo.socio_dni == dni, Prestamo.libro_isbn == isbn, Prestamo.devuelto == False).first()
            if prestamo:
                prestamo.devuelto = True
                prestamo.fecha_devolucion = datetime.now()
                libro.cantidad_disponible += 1
                socio.prestamos -= 1
                if socio.libros_prestados:
                    libros = socio.libros_prestados.split(",")
                    if isbn in libros:
                        libros.remove(isbn)
                        socio.libros_prestados = ",".join(libros) if libros else None
            self.DB.commit()
            return True
        else:
            return False

    
    def buscar_socio(self, dni):
        return self.DB.query(Socio).filter(Socio.dni == dni).first()
    
    def buscar_libro(self, isbn):
        return self.DB.query(Libro).filter(Libro.isbn == isbn).first()
    
    def listar_socios(self):
        return self.DB.query(Socio).all()
    
    def listar_libros(self):
        return self.DB.query(Libro).all()
    
    def listar_prestamos(self):
        return self.DB.query(Prestamo).all()
    
    def consultar_libros(self):
        return self.listar_libros()

    def consultar_usuarios(self):
        return self.listar_socios()
    
    def consultar_prestamos(self):
        return self.listar_prestamos()
    

    

