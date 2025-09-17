import os

file_name = 'sample.txt'
relative_path = 'assignment4/' + file_name
try :
    if os.path.exists(relative_path) : 
        read_file = open(relative_path, 'rt')
        print("\nReading file content:")
        print(f"\nLine 1: {read_file.readline()}")
        print(f"Line 2: {read_file.readline()}")
    else : 
        raise FileNotFoundError    
except Exception as e:
    print(f"\nError: The file {file_name} was not found.")
finally : 
    read_file.close()
    print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")        