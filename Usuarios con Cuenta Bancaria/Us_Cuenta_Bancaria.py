class CuentaBancaria:
    cuentas = []
    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def deposito(self, monto):
        self.balance += monto
        return self

    def retiro(self,monto):
        if(self.balance - monto) >= 0:
            self.balance -= monto
        else:
            print("Fondos Insifucientes: Cobro de $5 por movimiento")
            self.balance -= 5
        return self
    
    def mostrar_info_cuenta(self):
        return f"{self.balance}"

    def rentabilidad_intereses(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interes)
        return self

    @classmethod
    def mostrar_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()


class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cuenta = {
            "corriente" : CuentaBancaria(0.2,200000),
            "ahorros" : CuentaBancaria(0.1,100000)
        }
        

    def mostrar_balance_cuenta(self):
        print(f"Usuario: {self.nombre}, Balance Corriente: {self.cuenta['corriente'].mostrar_info_cuenta()}")
        print(f"Usuario: {self.nombre}, Balance Ahorros: {self.cuenta['ahorros'].mostrar_info_cuenta()}")
        return self

    def transferir_dinero(self, monto, usuario):
        self.monto -= monto
        usuario.monto += monto
        self.mostrar_balance_cuenta()
        usuario.mostrar_balance_cuenta()
        return self


javi = Usuario("Javi")

javi.cuenta['corriente'].deposito(100)
javi.mostrar_balance_cuenta()