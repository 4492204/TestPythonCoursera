class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im
    def __str__(self):
        return str(self.re) + '+' +str(self.im) + 'i'
a = Complex(1, 2)
b = Complex(3)
c = Complex()
print(b)