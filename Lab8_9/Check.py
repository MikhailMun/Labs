import random
import math
class Matrix:
    def __init__(self,rows,columns):
        self.rows = rows;
        self.columns = columns;
        self.matx = [];
        for i in range(self.rows):
            self.matx.append([]);
            for j in range(self.columns):
                self.matx[i].append(random.randint(0,5));

    def display(self):
        for i in range(self.rows):
            print(self.matx[i]);
        print('\n')

    def __add__(self, other):
        if (self.rows == other.rows) and (self.columns == other.columns):
            result = Matrix(self.rows,self.columns);
            for i in range(self.rows):
                for j in range(self.columns):
                    result.matx[i][j] = self.matx[i][j] + other.matx[i][j];
                return result
        else:
            print('Данные матрицы сложить нельзя');
            return 1

    def __sub__(self,other):
        if (self.rows == other.rows) and (self.columns == other.columns):
            result = Matrix(self.rows,self.columns);
            for i in range(self.rows):
                for j in range(self.columns):
                    result.matx[i][j] = self.matx[i][j] - other.matx[i][j];
                return result
        else:
            print('Данные матрицы нельзя вычесть друг из друга')
            return 1;

    def __mul__(self,other):
        if type(other).__name__ == 'int':
            result = Matrix(self.rows,self.columns);
            for i in range(self.rows):
                for j in range(self.columns):
                    result.matx[i][j] = self.matx[i][j] * other;
            return result
        elif self.columns == other.rows:
            result = Matrix(self.rows,other.columns);
            for i in range(self.rows):
                for j in range(other.columns):
                    thate = 0;
                    for k in range(self.columns):
                        thate += self.matx[i][k] * other.matx[k][j];
                    result.matx[i][j] = thate;
            return result
        else:
            print('Это действие невозможно:\nМатрицы не квадратные или происходит умножение не на число ')
            return 1;

    def trans(self):
        b = self.columns;
        self.columns = self.rows;
        self.rows = b
        result = Matrix(self.rows,self.columns);
        for i in range(self.rows):
            for j in range(self.columns):
                result.matx[i][j] = self.matx[j][i]
        self.matx = result.matx

    def det(self):
       if self.columns == self.rows:
           det, kof = 1, 1
           n = len(self.matx)
           for i in range(n):
               j = max(range(i, n), key=lambda k: abs(self.matx[k][i]))
               if i != j:
                  self.matx[i], self.matx[j] = self.matx[j], self.matx[i]
                  det *= -1
               if self.matx[i][i] == 0:
                   return 0
               det *= self.matx[i][i]
               for j in range(i + 1, n):
                   gcd = math.gcd(self.matx[i][i], self.matx[j][i])
                   b = self.matx[j][i] // gcd
                   c = self.matx[i][i] // gcd
                   kof *= c
                   self.matx[j] = [c * self.matx[j][k] - b * self.matx[i][k] for k in range(n)]
           return det // kof
       else:
           return print('Нельзя найти определитель неквадратных матриц матриц')
