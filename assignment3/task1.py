def factorial(num) :
    """
    Recurvise calculate the factorial of a num
    :return: int
    """
    if num <= 1 :
        return 1
    else :
        return num * factorial(num-1)

try :
    num = int(input("Enter a number: "))    
    if num < 0 :
        raise ValueError()
    else :
        fact = factorial(num)

        print(f"Factorial of {num} is: {fact}")
except ValueError as ve :
    print(f"\nCan't calculate factorial for negative integer")        
except Exception as e: 
    print(f"\nError: Not a valid number, {e}")
finally :
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")        