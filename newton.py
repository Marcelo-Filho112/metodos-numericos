import math

class Newton:
    def __init__(self, xo, stop):
        self.xo = xo  # Ponto inicial (t0 = 0)
        self.stop = stop  # Critério de parada (erro relativo)
        self.state = True
        self.x = None

    def function(self, t):
        # f(t) = 9e^(-t) * sin(2πt) - 3.5
        return 9 * math.exp(-t) * math.sin(2 * math.pi * t) - 3.5

    def realfunction(self, t):
        # f(t) = 9e^(-t) * sin(2πt)
        return 9 * math.exp(-t) * math.sin(2 * math.pi * t)

    def derivate(self, t):
        # Derivada de f(t) = 9e^(-t) * sin(2πt) - 3.5
        return 9 * (-math.exp(-t) * math.sin(2 * math.pi * t) + 2 * math.pi * math.exp(-t) * math.cos(2 * math.pi * t))

    def iterate(self):
        while self.state:
            # Aplica a fórmula de Newton: t = t0 - f(t0)/f'(t0)
            f_t = self.function(self.xo)
            f_prime_t = self.derivate(self.xo)
            if f_prime_t == 0:  # Verificação de divisão por zero
                raise ValueError("Derivada é zero, método de Newton falha.")
            
            self.x = self.xo - f_t / f_prime_t

            # Verifica se atingiu o critério de parada
            error = self.relative_error(self.x)
            self.state = self.comparate(error)

            self.xo = self.x  # Atualiza o valor de t0 para a próxima iteração

    def comparate(self, error):
        return error >= self.stop

    def relative_error(self, x):
        return abs(self.x - self.xo) / abs(self.x) if self.x != 0 else float('inf')

# Exemplo de uso
newton_solver = Newton(xo=0, stop=1e-6)
newton_solver.iterate()
print(f"Menor valor de t para i = 3.5: {newton_solver.x}")
print(newton_solver.realfunction(newton_solver.x))
