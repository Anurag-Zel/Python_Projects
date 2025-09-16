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
    num = int(input("\nEnter a number: "))    
    if num < 0 :
        raise ValueError()
    else :
        fact = factorial(num)

        print(f"Factorial of {num} is: {fact}")        
except Exception as e: 
    print(f"\nError: Not a valid number. Enter integer greater equal than 0")
finally :
    print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")        