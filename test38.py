class Fraction:
    def __init__(self, s, m):
        self.soorat = s
        self.makhraj = m

    def show(self):
        print(self.soorat, '/', self.makhraj)

    def mul(self, f):
        result = Fraction(None, None)
        result.soorat = self.soorat * f.soorat
        result.makhraj = self.makhraj * f.makhraj
        return result

    def sum(self, f):
        result = Fraction(None, None)
        result.soorat = (self.soorat * f.makhraj) + (f.soorat * self.makhraj)
        result.makhraj = (self.makhraj * f.makhraj)
        return result

    def div(self, f):
        result = Fraction(None, None)
        result.soorat = (self.soorat * f.makhraj)
        result.makhraj = (self.makhraj * f.soorat)
        return result

    def sub(self, f):
        result = Fraction(None, None)
        result.soorat = (self.soorat * f.makhraj) - (self.makhraj * f.soorat)
        result.makhraj = self.makhraj * f.makhraj
        return result

fraction1 = Fraction(2, 3)
fraction1.show()

fraction2 = Fraction(3, 5)
fraction2.show()

result_mul = fraction1.mul(fraction2)
result_mul.show()


result_sum = fraction1.sum(fraction2)
result_sum.show()

result_div = fraction1.div(fraction2)
result_div.show()

result_sub = fraction1.sub(fraction2)
result_sub.show()