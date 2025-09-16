import math

try : 
    num = int(input("\nEnter a number: "))
    sqrt = math.sqrt(num)
    log = math.log(num)
    sin = math.sin(num)

    print(f"\nSquare root: {sqrt} \nLogarithm: {log} \nSine: {sin}")
       
except Exception as e: 
    print(f"\nError: Not a valid number. Enter integer greater than 0")
finally :
    print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")    