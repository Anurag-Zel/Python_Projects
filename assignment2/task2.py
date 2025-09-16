try :
    sum = 0
    for i in range(1,51):
        sum += i

    print(f"\nThe sum of numbers from 1 to 50 is: {sum}")    
except Exception as e: 
    print(f"\nError: {e}")
finally :
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")      