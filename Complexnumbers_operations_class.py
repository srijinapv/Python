import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, number2):
        result_add = Complex(self.real + number2.real, self.imaginary +number2.imaginary)
        return result_add

    def __sub__(self, number2):
        return Complex(self.real - number2.real, self.imaginary - number2.imaginary)

    def __mul__(self, number2):
        return Complex(self.real*number2.real - self.imaginary*number2.imaginary,
                       self.imaginary*number2.real + self.real*number2.imaginary)

    def __truediv__(self,  number2):
        sr, si, nr, ni = self.real, self.imaginary,number2.real, number2.imaginary # short forms
        r = float(nr**2 + ni**2)
        return Complex((sr*nr+si*ni)/r, (si*nr-sr*ni)/r)


    def mod(self):
        #return math.sqrt(self.real**2 + self.imaginary**2 )
        a1 = math.sqrt(self.real**2 + self.imaginary**2 )
        b1 = round(a1,2)
        c1 = format(0.0, '.2f')
        return(f'{b1}+{c1}i')

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')