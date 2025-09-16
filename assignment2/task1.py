try :
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(f"\n{num} is an even number.")
    else:
        print(f"\n{num} is an odd number.")   
except Exception as e: 
    print(f"\nError: Not a valid number, {e}")
finally :
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")       