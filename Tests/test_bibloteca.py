import pytest
from Biblioteca.libro import Libro
from Biblioteca.socio import Socio
from Biblioteca.prestamo import Prestamo
from datetime import datetime
from database import SessionLocal, Base, engine
from Biblioteca.biblioteca import biblioteca

@pytest.fixture(scope="module")
def configurar_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    yield db
    
    db.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def instancia_biblioteca(configurar_db):
    return biblioteca()

def test_alta_socio(instancia_biblioteca, configurar_db):
    dni = "12345678A"
    nombre = "Juan Pérez"
    telefono = "555-1234"
    correo = "juan.perez@correo.com"

    assert instancia_biblioteca.alta_socio(dni, nombre, telefono, correo) == True
    
    socio = configurar_db.query(Socio).filter(Socio.dni == dni).first()
    assert socio is not None
    assert socio.nombre == nombre

def test_baja_socio(instancia_biblioteca, configurar_db):
    dni = "12345678B"
    instancia_biblioteca.alta_socio(dni, "Maria López", "555-5678", "maria.lopez@correo.com")

    socio = configurar_db.query(Socio).filter(Socio.dni == dni).first()
    assert socio is not None

    assert instancia_biblioteca.baja_socio(dni) == True
    
    socio = configurar_db.query(Socio).filter(Socio.dni == dni).first()
    assert socio is None

def test_alta_libro(instancia_biblioteca, configurar_db):
    isbn = "978-3-16-148410-0"
    titulo = "El Gran Libro"
    autor = "Autor Ejemplo"
    editorial = "Editorial Ejemplo"
    genero = "Ficción"
    cantidad = 5

    assert instancia_biblioteca.alta_libro(isbn, titulo, autor, editorial, genero, cantidad) == True
    
    libro = configurar_db.query(Libro).filter(Libro.isbn == isbn).first()
    assert libro is not None
    assert libro.titulo == titulo

def test_baja_libro(instancia_biblioteca, configurar_db):
    isbn = "978-3-16-148410-1"
    instancia_biblioteca.alta_libro(isbn, "Libro para Baja", "Autor Ejemplo", "Editorial", "Ficción", 3)

    libro = configurar_db.query(Libro).filter(Libro.isbn == isbn).first()
    assert libro is not None

    assert instancia_biblioteca.baja_libro(isbn) == True
    
    libro = configurar_db.query(Libro).filter(Libro.isbn == isbn).first()
    assert libro is None

def test_prestamo_libro(instancia_biblioteca, configurar_db):
    dni = "12345678C"
    instancia_biblioteca.alta_socio(dni, "Carlos García", "555-9876", "carlos.garcia@correo.com")
    
    isbn = "978-3-16-148410-2"
    instancia_biblioteca.alta_libro(isbn, "Libro para Préstamo", "Autor Ejemplo", "Editorial", "Ficción", 5)

    assert instancia_biblioteca.prestamo_libro(dni, isbn) == True
    
    libro = configurar_db.query(Libro).filter(Libro.isbn == isbn).first()
    assert libro.cantidad_disponible == 4

    socio = configurar_db.query(Socio).filter(Socio.dni == dni).first()
    assert socio.prestamos == 1

def test_devolucion_libro(instancia_biblioteca, configurar_db):
    dni = "12345678D"
    instancia_biblioteca.alta_socio(dni, "Ana Rodríguez", "555-4321", "ana.rodriguez@correo.com")
    
    isbn = "978-3-16-148410-3"
    instancia_biblioteca.alta_libro(isbn, "Libro para Devolución", "Autor Ejemplo", "Editorial", "Ficción", 5)
    
    instancia_biblioteca.prestamo_libro(dni, isbn)
    
    assert instancia_biblioteca.devolucion_libro(dni, isbn) == True
    
    libro = configurar_db.query(Libro).filter(Libro.isbn == isbn).first()
    assert libro.cantidad_disponible == 5

    socio = configurar_db.query(Socio).filter(Socio.dni == dni).first()
    assert socio.prestamos == 0
