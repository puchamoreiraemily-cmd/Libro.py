# El "Molde" (La Clase)
class Libro:
    
    # Aquí definimos las 3 características (Atributos)
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo       # Atributo 1
        self.autor = autor         # Atributo 2
        self.paginas = paginas     # Atributo 3

    # Aquí definimos la Acción 1 (Método 1)
    def mostrar_informacion(self):
        print(f"Este libro se llama {self.titulo} y lo escribió {self.autor}.")

    # Aquí definimos la Acción 2 (Método 2)
    def leer(self):
        print(f"Estás leyendo '{self.titulo}'... ¡Qué buena lectura!")


# ==========================================
# AQUÍ CREAMOS LOS OBJETOS REALES
# ==========================================

# Creamos el primer libro real (Objeto 1)
libro1 = Libro("Harry Potter", "J.K. Rowling", 300)

# Creamos el segundo libro real (Objeto 2)
libro2 = Libro("Don Quijote", "Miguel de Cervantes", 800)


# ==========================================
# AQUÍ PROBAMOS QUE FUNCIONA
# ==========================================
libro1.mostrar_informacion()  # Le pedimos al libro 1 que muestre su info
libro1.leer()                 # Le pedimos al libro 1 que haga la acción de leer
