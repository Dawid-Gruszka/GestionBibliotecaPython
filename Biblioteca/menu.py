class menu:

    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
        self.ejecutando = True
    
    def mostrar_menu(self):
        while self.ejecutando:
            print("Bienvenido a la biblioteca")
            print("1.Alta de Socio")
            print("2.Baja de Socio")
            print("3.Alta de Libro")
            print("4.Baja de Libro")
            print("5.Prestamo de Libro")
            print("6.Devolucion de Libro")
            print("7.Consultar Libros")
            print("8.Consultar Usuarios")
            print("9.Consultar Prestamos")
            print("10.Salir")
            seleccion = input("Ingrese una opcion: ")

            if seleccion == "1":
                self.alta_socio()
            elif seleccion == "2":
                self.baja_socio()
            elif seleccion == "3":
                self.alta_libro()
            elif seleccion == "4":
                self.baja_libro()
            elif seleccion == "5":
                self.prestamo_libro()
            elif seleccion == "6":
                self.devolucion_libro()
            elif seleccion == "7":
                self.consultar_libros()
            elif seleccion == "8":
                self.consultar_usuarios()
            elif seleccion == "9":
                self.consultar_prestamos()
            elif seleccion == "10":
                self.ejecutando = False
            else:
                print("Error, opcion invalida")

    def alta_socio(self):
        print("Introduce DNI: ")
        dni = input()
        print("Introduce nombre: ")
        nombre = input()
        print("Introduce telefono: ")
        telefono = input()
        print("Introduce correo: ")
        correo = input()

        if self.biblioteca.alta_socio(dni, nombre, telefono, correo):
            print("Socio dado de alta")
        else:
            print("Error al dar de alta el socio")
    
    def baja_socio(self):
        print("Introduce DNI: ")
        dni = input()
        if self.biblioteca.baja_socio(dni):
            print("Socio dado de baja")
        else:
            socio = self.biblioteca.buscar_socio(dni)
            if socio:
                print("Error, el socio tiene libros prestados")
            else:
                print("Socio no encontrado")

    def alta_libro(self):
        print("Introduce ISBN: ")
        isbn = input()
        print("Introduce titulo: ")
        titulo = input()
        print("Introduce autor: ")
        autor = input()
        print("Introduce editorial: ")
        editorial = input()
        print("Introduce genero: ")
        genero = input()
        print("Introduce cantidad: ")
        cantidad = int(input())

        if self.biblioteca.alta_libro(isbn, titulo, autor, editorial, genero, cantidad):
            print("Libro dado de alta")
        else:
            print("Error al dar de alta el libro")
    
    def baja_libro(self):
        print("Introduce ISBN: ")
        isbn = input()
        if self.biblioteca.baja_libro(isbn):
            print("Libro dado de baja")
        else:
            print("Libro no encontrado o esta prestado")

    def prestamo_libro(self):
        print("Introduce DNI: ")
        dni = input()
        print("Introduce ISBN: ")
        isbn = input()

        if self.biblioteca.prestamo_libro(dni, isbn):
            print("Libro prestado")
        else:
            print("Error al prestar el libro")
    
    def devolucion_libro(self):
        print("Introduce DNI: ")
        dni = input()
        print("Introduce ISBN: ")
        isbn = input()

        if self.biblioteca.devolucion_libro(dni, isbn):
            print("Libro devuelto")
        else:
            print("Error al devolver el libro")
    
    def consultar_libros(self):
        libros = self.biblioteca.consultar_libros()
        print("Libros disponibles: ")
        if libros:
            for libro in libros:
                print(libro)
        else:
            print("No hay libros disponibles")
    
    def consultar_usuarios(self):
        usuarios = self.biblioteca.consultar_usuarios()
        print("Usuarios: ")
        if usuarios:
            for usuario in usuarios:
                print(usuario)
        else:
            print("No hay usuarios")
    
    def consultar_prestamos(self):
        prestamos = self.biblioteca.consultar_prestamos()
        print("Prestamos: ")
        if prestamos:
            for prestamo in prestamos:
                print(prestamo)
        else:
            print("No hay prestamos")

        

            