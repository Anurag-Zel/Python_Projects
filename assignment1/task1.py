
try :
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2

    print(f"\n\nAddition: {add} \nSubtraction: {sub} \nMultiplication: {mul} \nDivision: {div}")
except Exception as e :
    print(f"\nError: Not a valid number, {e}")    
finally :    
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

