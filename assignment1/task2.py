try :
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")

    if len(fname) == 0 and len(lname) == 0:
        raise Exception("\n\nError : Enter atleast one character")
    else :
        print(f"\n\nHello, {fname + ' ' + lname}! Welcome to the Python program")    
except Exception as e :
    print(f"\n Error: {e}")
finally : 
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")        