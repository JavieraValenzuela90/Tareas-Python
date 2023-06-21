class CuentaBancaria:
    cuentas = []
    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def deposito(self, monto):
        self.balance += monto
        return self

    def retiro(self, monto):
        if(self.balance - monto) >= 0:
            self.balance -= monto
        else:
            print("Fondos Insifucientes: Cobro de $5 por movimiento")
            self.balance -= 5
        return self
    
    def mostrar_info_cuenta(self):
        print(f"Balance: {self.balance}")
        return self

    def rentabilidad_intereses(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interes)
        return self

    @classmethod
    def mostrar_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()


ahorros = CuentaBancaria(0.2,20000)
cuenta_corriente = CuentaBancaria(0.1,100000)

ahorros.deposito(1000).deposito(200).deposito(3000).retiro(500).rentabilidad_intereses().mostrar_info_cuenta()
cuenta_corriente.deposito(10000).deposito(2000).deposito(1000).retiro(250).rentabilidad_intereses().mostrar_info_cuenta()

CuentaBancaria.mostrar_cuentas()