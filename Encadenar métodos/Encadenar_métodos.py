class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.monto = 0
    def hacer_deposito(self, deposito):
        self.monto += deposito
        return self
    def hacer_retiro(self, retiro):
        self.monto -= retiro
        return self
    def mostrar_balance_usuario(self):
        print("Usuario: " + self.nombre + ", Balance: $" + str(self.monto))
    def transfer_dinero(self, otro_usuario, monto):
        self.hacer_retiro(monto)
        otro_usuario.hacer_deposito(monto)
    

javi = Usuario("Javi Valenzuela")
coni = Usuario("Coni Valenzuela")
benja = Usuario("Benja Cofré")
javi.hacer_deposito(100).hacer_deposito(200).hacer_deposito(300).hacer_retiro(50).mostrar_balance_usuario()


