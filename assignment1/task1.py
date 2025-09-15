
try :
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2

    print(f"\nAddition: {add} \nSubtraction: {sub} \nMultiplication: {mul} \nDivision: {div}")
except ZeroDivisionError :
    print("Division by zero, not defined.")
except Exception as e :
    print(f"Please enter a valid number, {e}")    
finally :    
    print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

