class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.monto = 0
    def hacer_deposito(self, deposito):
        self.monto += deposito
    def hacer_retiro(self, retiro):
        self.monto -= retiro
    def mostrar_balance_usuario(self):
        print("Usuario: " + self.nombre + ", Balance: $" + str(self.monto))
    def transfer_dinero(self, otro_usuario, monto):
        self.hacer_retiro(monto)
        otro_usuario.hacer_deposito(monto)
    

javi = Usuario("Javi Valenzuela")
coni = Usuario("Coni Valenzuela")
benja = Usuario("Benja Cofré")
javi.hacer_deposito(100)
javi.hacer_deposito(100)
javi.hacer_deposito(100)
javi.hacer_retiro(50)
javi.mostrar_balance_usuario()
coni.hacer_deposito(500)
coni.hacer_deposito(100)
coni.hacer_retiro(100)
coni.hacer_retiro(100)
coni.mostrar_balance_usuario()
benja.hacer_deposito(1000)
benja.hacer_retiro(100)
benja.hacer_retiro(500)
benja.hacer_retiro(100)
benja.mostrar_balance_usuario()
javi.transfer_dinero(benja, 50)
javi.mostrar_balance_usuario()
benja.mostrar_balance_usuario()

