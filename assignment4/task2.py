try :
    output_file = 'output.txt'
    output_path = 'assignment4/' + output_file
    file = open(output_path, 'wt')

    string1 = input("\nEnter text to write to the file: ")
    file.write(string1 + "\n")
    print(f'Data successfully written to {output_file}.')

    string2 = input("\nEnter additional text to append: ")
    file.write(string2 + "\n")
    print('Data successfully appended.')

    file.close()
    file = open(output_path, 'rt')
    print(f'\nFinal content of {output_file}')
    print(file.read())

except Exception as e :
    print(f"\nError: Error occured while appending.")
finally : 
    file.close()
    print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")        