from database import Base, engine
from Biblioteca.biblioteca import biblioteca
from Biblioteca.menu import menu
class main:

    biblioteca = biblioteca()
    menu = menu(biblioteca)
    Base.metadata.create_all(bind=engine)
    menu.mostrar_menu()

if __name__ == "__main__":
    main()