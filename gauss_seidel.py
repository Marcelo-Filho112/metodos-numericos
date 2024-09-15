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
        sum = 0
        for j in range(len(self.A)):
            if i != j:
                print(f"x[{j}] = {self.x[j]}")
                print(f"A[{i}][{j}] = {self.A[i][j]}")
                sum  += self.x[j]*self.A[i][j]
        print(f"b[{i}] = {self.b[i]}")
        sum = self.b[i] - sum
        print(round(sum/self.A[i][i], 4))
        return round(sum/self.A[i][i], 4)


    def iterate(self):
        while self.state:
            self.count += 1
            print(self.count)
            for i in range(len(self.A)):
                self.x[i] = self.calculate(i)
            self.state = self.error()
            self.update()


    def update(self):
        self.y = np.copy(self.x)

    def error(self):
        error = np.round(self.maxNum()/self.maxDem())
        return error >= self.stop
                

    def maxDem(self):
        return np.max(np.abs(self.x))

    def maxNum(self):
        return np.max(np.abs(self.x - self.y))


A = np.array([
    [5, 1, 1],
    [3, 4, 1],
    [3, 3 ,6]
])

b = np.array([5, 6, 0])

x = np.array([0, 0, 0])

gauss_solver = GaussSeidel(A,x,b,0.05)
gauss_solver.iterate()
formatted_solution = [f"{xi:.4f}" for xi in gauss_solver.x]
print(f"vetor solução: {formatted_solution}")
print(f"numero de iterações: {gauss_solver.count}")
#Exemplo prático
# A = np.array([
#     [17, -5,  0,  0,  0,  0, 0,  -2],
#     [ 1, -4,  2,  0,  0,  0,  1,  0],
#     [ 0,  6, -9,  2,  0,  1,  0,  0],
#     [ 0,  0,  1, -4,  3,  0,  0,  0],
#     [ 0,  0,  0,  8, -9,  1,  0,  0],
#     [ 0,  0,  4,  0,  3, -10,  3,  0],
#     [ 0, 12,  0,  0,  0,  3, -23,  8],
#     [ 6,  0,  0,  0,  0,  0,  10, -31]
# ])

# b = np.array([1000, 0, 0, 0, 0, 0, 0, 0])

# x = np.array([0, 0, 0, 0, 0, 0, 0, 0])