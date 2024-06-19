# import sqlite3
import sqlite3

# to execute the SQl statement you nee to use this, the fellowing fuction below
create_sql = sqlite3.connect("Data-Base/user_data.db")
execute_cursor = create_sql.cursor()

# it verfys is the table "address" in the database been created or not
def verfy_table():
    verfy_table = execute_cursor.execute("SELECT name FROM sqlite_master")
    verfy_table = verfy_table.fetchone()

    return verfy_table

def insert_data():
    execute_cursor.execute("""
        INSERT INTO address VALUES
            ('Agha Muhammad', 'Imran', 07479963321),
            ('Aaron', 'gregory', 07479963321)
    """)
    return "Data inserted in the table"


#this functions checks if the data is inserted in the table,
def verfy_data_in_table():
    verfy_data = execute_cursor.execute("SELECT  phone_number FROM address")
    verfy_data = verfy_data.fetchall()
    return verfy_data


# im using "try" statement here to prevent errors, when the table already exists
try:

    # this code creates the table "address" in the database
    execute_cursor.execute("CREATE TABLE address(First_name, Last_name, phone_number )")
    insert_data()


except:

    print("Table 'address' has been created")
    verfy_data_insert = insert_data()
    print(verfy_data_insert)

check_DataBase_table = verfy_table()
print(check_DataBase_table)

check_inserted_data = verfy_data_in_table()
print(check_inserted_data)














#
# # to execute the SQl statement you nee to use this, the fellowing fuction below
# create_sql = sqlite3.connect("Data-Base/user_data.db")
# execute_cursor = create_sql.cursor()
#
#
#
#
#
# # it verfys is the table "address" in the database been created or not
# def verfy_table():
#     verfy_table = execute_cursor.execute("SELECT name FROM sqlite_master")
#     verfy_table = verfy_table.fetchone()
#
#
#
#     return verfy_table
#
# def insert_data():
#     execute_cursor.execute("""
#         INSERT INTO address VALUES
#             ('Agha Muhammad', 'Imran', 07479963321),
#             ('Aaron', 'gregory', 07479963321)
#     """)
#
#     return "Data inserted in the table"
#
# # Test function: how to add three more rows
# def insert_three_rows():
#     users = [
#         ('Alice', 'Smith', '555-1234'),
#         ('Bob', 'Johnson', '555-5678'),
#         ('Charlie', 'Williams', '555-8765')
#     ]
#     execute_cursor.executemany("INSERT INTO address VALUES(?, ?, ?)", users)
#
#
#
# #this functions checks if the data is inserted in the table, "SELECT score FROM movie"
# def verfy_data_in_table():
#     verfy_data = execute_cursor.execute("SELECT  phone_number FROM address")
#     verfy_data = verfy_data.fetchall()
#
#
# # to check the row using for loop
#     for row in  verfy_data:
#         print(row)
#     return verfy_data
#
#
# # im using "try" statement here to prevent errors, when the table already exists
# try:
#
#     # this code creates the table "address" in the database
#     execute_cursor.execute("CREATE TABLE address(First_name, Last_name, phone_number )")
#     insert_three_rows()
#
# except:
#     print("Table 'address' has been created")
#     verfy_data_insert = insert_three_rows()
#     print(verfy_data_insert)
#
# check_DataBase_table = verfy_table()
# print(check_DataBase_table)
#
# check_inserted_data = verfy_data_in_table()
# print(check_inserted_data)
#
#
#
#
#
#
#
#
#
#
#
#



