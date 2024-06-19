import sqlite3

create_sql = sqlite3.connect("AddressBook-DataBase/User-address-book")
execute_cursor = create_sql.cursor()

#
# class User:
#     def __init__(self, First_name,Last_name,phone_number):
#         self.First_name = First_name
#         self.Last_name = Last_name
#         self.phone_number = phone_number
#
#

#this funtion adds new user to the table "address"
def insert_user_in_table(First_name, Last_name, phone_number):
    execute_cursor.execute(f"""
    INSERT INTO address VALUES
       ('{First_name}', '{Last_name}', {int(phone_number)})
    """)
    return "Data inserted in the table"

#this functions checks if the data is inserted in the table,
def verfy_data_in_table():
    verfy_data = execute_cursor.execute("SELECT  First_name, Last_name, phone_number FROM address")
    verfy_data = verfy_data.fetchall()
    return verfy_data

try:
    # this code creates the table "address" in the database
    execute_cursor.execute("CREATE TABLE address(First_name, Last_name, phone_number )")
except:
    pass

