# Multiple Inheritance:
# In this example, the class C is inheriting the properties of the class A and B.

class A:
    varA = 'Welcome to class A'

class B:
    varB = 'Welcome to class B'

class C(A, B):
    varC = 'Welcome to class C'

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)
