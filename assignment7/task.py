import pg8000

try : 
    conn = pg8000.connect(database="postgres", user="postgres", password="Darkzel@008", host="localhost", port=5432)
    print("\nDatabase Connected")

    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE employess(Name Text, ID int, Age int); ''')
    cursor.execute(''' INSERT INTO employess(Name,ID,Age) values ('Alex',02,25)''')
    # cursor.execute(''' SELECT * FROM employess ; ''')
    # print(cursor.fetchall())

    name = input("\nEnter name : ")
    age = int(input("\nEnter age : "))
    ID = int(input("\nEnter Id : "))

    query = ''' INSERT INTO employess(Name,ID,Age) values (%s,%s,%s)'''
    cursor.execute(query,(name,ID,age))

    conn.commit()
    # print("\nTable Created Successfully.")
    print("\nTable Updated Successfully.")
    # print("\nData Extracted Successfully.")
    
except Exception as e: 
    print(f"\n {e}")
finally : 
    print("\nClosing database connection")
    conn.close()