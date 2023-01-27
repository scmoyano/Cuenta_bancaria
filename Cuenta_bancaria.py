
class Persona:

    #En la clase perosna se almacenaran los datos personales de los usuarios

    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido



class Cliente(Persona):
    #La clase cliente hereda de Persona y permite realizar operaciones bancarias
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: ${self.balance}"

    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Monto depositado")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")

""" 
funcion crear un clente
"""

def crear_cliente():

   nombre_cl = input("Por favor ingrese su nombre")
   apellido_cl = input("Por favor ingrese su apellido") 
   numero_cuenta = input("ingrese su numero de cuenta") 
   cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta)
   return cliente



def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print('Elije: Depositar (D), Retirar (R), o Salir (S)')
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)

    print("Gracias por operar en Banco del sueño")


inicio()




