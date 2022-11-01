#Pregunta 01 Crear un programa de evaluación de pago de impuestos.

class Persona:
    def __init__(self):
        self.nombre=input("Ingrese su nombre: ")
        self.edad=int(input("Ingrese su edad: "))
 
     # declaramos el metodo para imprimir
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
    
 
# declaramos la clase empleado
class Empleado(Persona):
    def __init__(self):
        # llamamos al metodo init de la clase padre
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo: "))
 
        # declaramos el metodo mostrar
    def mostrar(self):
        super().mostrar()
        print("Sueldo: ",self.sueldo)

        # declaramos el metodo pagar_impuestos
    def pagar_impuestos(self):
        impuesto =(self.sueldo*9)/100
        print("el impuesto del empleado es: ", impuesto)
        if self.sueldo > 45000:
            print("El empleado debe pagar impuestos.")
        else:
            print("El empleado no paga impuestos.")
 

 # para ejecutar   
persona1=Persona()
empleado1=Empleado()
persona1.mostrar()
empleado1.mostrar()
empleado1.pagar_impuestos()
empleado1.manejo_diccionario()