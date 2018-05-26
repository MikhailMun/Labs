from Check import Matrix
A = Matrix(3, 4)
B = Matrix(4, 3)
print("A")
A.display()
print("B")
B.display()
C = A + B
print("C = A + B")
if C != 1:
    C.display()
D = A - B
print("D = A - B")
if D != 1:
    D.display()
E = A * 2
print("E = A * 2")
if E != 1:
    E.display()
F = A * B
print("F = A * B")
if F != 1:
    F.display()
A.trans()
print("A^T")
A.display()
detA = A.det()
if detA != 'string':
    print("Det A = " + str(detA))
