import math

class Secante:
    def __init__(self,xo,x1,error):
        self.xo = xo
        self.x1 = x1
        self.error = error
        self.state = True

    def function(self, x):
        # f(t) = 9e^(-t) * sin(2πt) - 3.5
        return 9 * math.exp(-x) * math.sin(2 * math.pi * x) - 3.5
    
    def realfunction(self, x):
        # f(t) = 9e^(-t) * sin(2πt)
        return 9 * math.exp(-x) * math.sin(2 * math.pi * x)

    def iterate(self):

        while self.state:
            # Cálculo do numerador
            num1 = self.xo*self.function(self.x1)
            num2 = self.x1*self.function(self.xo)
            # Cálculo do denominadar
            dem1 = self.function(self.x1)
            dem2 = self.function(self.xo)
            #Atribuição de novos valores para xk-1 e xk
            self.xo = self.x1
            self.x1 = (num1-num2)/(dem1-dem2)

            error = self.relative_error(self.x1)
            self.state = self.comparate(error)


    
    def comparate(self, error):
        return error >= self.error

    def relative_error(self, x):
        return abs(self.x1 - self.xo) / abs(self.x1) if self.x1 != 0 else float('inf')

# Exemplo de uso
secante_solver = Secante(xo=0, x1=0.2, error=1e-6)
secante_solver.iterate()
print(f"Menor valor de t para i = 3.5: {secante_solver.x1}")
print(secante_solver.realfunction(secante_solver.x1))
