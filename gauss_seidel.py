import math
import numpy as np

class GaussSeidel():
    def __init__(self, A, x, b, stop):
        self.A = A
        self.x = x
        self.y = np.copy(x)
        self.b = b
        self.state = True
        self.stop = stop
        self.count = 0

    def calculate(self, i):
        # Cálculo dos somatório entre aij, xj e bi
        sum = 0
        for j in range(len(self.A)):
            if i != j:
                sum  += self.x[j] * self.A[i][j]
        sum = self.b[i] - sum
        # Retorna valor de xi novo
        return round(sum/self.A[i][i], 4)

    def iterate(self):
        # Aplicação do Método de Gauss-Seidel
        while self.state:
            self.count += 1
            for i in range(len(self.A)):
                self.x[i] = self.calculate(i)
            self.state = self.error()
            self.update()

    def update(self):
        self.y = np.copy(self.x)

    def error(self):
        # Cálculo do erro relativo
        error = round(self.maxNum()/self.maxDem())
        return error >= self.stop

    def maxDem(self):
        return max(abs(self.x))

    def maxNum(self):
        return max(abs(self.x - self.y))


#Exemplo de uso
A = np.array([
    [17.0, -5.0,  0.0,  0.0,  0.0,  0.0, 0.0,  -2.0],
    [ 1.0, -4.0,  2.0,  0.0,  0.0,  0.0,  1.0,  0.0],
    [ 0.0,  6.0, -9.0,  2.0,  0.0,  1.0,  0.0,  0.0],
    [ 0.0,  0.0,  1.0, -4.0,  3.0,  0.0,  0.0,  0.0],
    [ 0.0,  0.0,  0.0,  8.0, -9.0,  1.0,  0.0,  0.0],
    [ 0.0,  0.0,  4.0,  0.0,  3.0, -10.0,  3.0,  0.0],
    [ 0.0, 12.0,  0.0,  0.0,  0.0,  3.0, -23.0,  8.0],
    [ 6.0,  0.0,  0.0,  0.0,  0.0,  0.0,  10.0, -31.0]
])

b = np.array([1000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

x = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

gauss_solver = GaussSeidel(A,x,b,1e-6)
gauss_solver.iterate()
formatted_solution = [f"{xi:.4f}" for xi in gauss_solver.x]
print(f"vetor solução: {formatted_solution}")
print(f"numero de iterações: {gauss_solver.count}")
