class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator
f1 = Fraction(1, 2)
f2 = Fraction(2, 4)
print(f1 == f2)  # True

