import sys 
sys.path.insert(0, "C:\\Users\\zhadb\\Downloads\\zhadba_Programs\\packaging-framework\\src\\example_package")

from calculator import Calculator

calculator_app = Calculator(5, 5)
sum = calculator_app.add()
difference = calculator_app.subtract()
product = calculator_app.multiply()
quotient = calculator_app.divide()

print(f"Sum: {sum}\nDifference {difference}\nProduct: {product}\nQuotient: {quotient}")