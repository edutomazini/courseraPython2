class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        return (self.a + self.b + self.c)

    def tipo_lado(self):
        if (self.a == self.b and self.b == self.c and self.c == self.a):
            return 'equilátero'
        if (self.a != self.b and self.b != self.c and self.c != self.a):
            return 'escaleno'
        if ((self.a == self.b and self.b!=self.c) or (self.a == self.c and self.a != self.b) or (self.b == self.c and self.b != self.a)):
            return 'isósceles'
        
t = Triangulo(5,8,5)
print('a',t.a)

print(t.perimetro())
print(t.tipo_lado())