class Fraction:

    def __init__(self , numerator , denominator):

        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self ,other):
        if isinstance(other , Fraction):
            new_numerator = (self.numerator*other.denominator)+ (other.numerator*self.denominator)
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator , new_denominator)
        else:
            raise TypeError("Operand must be an instance of Fraction")
    
    def __sub__(self ,other):
        if isinstance(other , Fraction):
            new_numerator = (self.numerator*other.denominator)-(other.numerator*self.denominator)
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator , new_denominator)
        else:
            raise TypeError("Operand must be an instance of Fraction")
        
    def __mul__(self,other):
        if isinstance(other ,Fraction):
            new_numerator = self.numerator*other.numerator
            new_denominator = self.denominator*other.denominator
            return Fraction(new_numerator , new_denominator)
        else:
            raise TypeError("Operand must be an instance of Fraction")
    

x = Fraction(3, 4)
print(x)  

y = Fraction(2, 5)
print(y)

print(x + y)
print(x - y)
print(x*y)