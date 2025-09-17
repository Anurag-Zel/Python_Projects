student_list = {"Alice": 75,"Bob": 80,"Chris": 67,"Diana": 92,"Ethan": 88,"Fiona": 73,"George": 85,"Hannah": 90,"Ian": 69,"Julia": 95,"Kevin": 78,"Laura": 82,"Mike": 70,"Nina": 87,"Oscar": 76,"Paula": 91,"Quentin": 68,"Rachel": 89,"Sam": 84,"Tina": 77,"Uma": 93,"Victor": 79,"Wendy": 86,"Zack": 81,}

try :
    student_name = input("\nEnter the student's name: ")
    marks = student_list[student_name]

    print(f'{student_name}\'s marks: {marks}')
except Exception as e :
    print("Student not found.")
finally : 
    print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")        