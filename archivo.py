class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        self.mensaje = "hola"

    def imprimir(self):
        print(f"{self.numerador}/{self.denominador}")

    def suma (self, fraccion_adicional):
        num_resultante = self.numerador * fraccion_adicional + fraccion_adicional.numerador * self.denominador
        den_resultante = self.denominador * fraccion_adicional.denominador
        resultado = Fraccion(num_resultante, den_resultante)
        return resultado

fraccion_uno = Fraccion(1,2)
fraccion_dos = Fraccion(3,4)
fraccion_uno.imprimir()
fraccion_dos.imprimir()

fraccion_resultante = fraccion_uno.suma(fraccion_dos)
fraccion_resultante.imprimir()

