from SQL_lite_database_center import *


# class student:
#     def __init__(self, name, phone_number, email, post_code,Birthday,Company, Job_Title , Notes):
#         self.name = name
#         self.phone_number = phone_number
#         self.email = email
#         self.post_code = post_code
#         self.Birthday = Birthday
#         self.Company = Company
#         self.Job_Title = Job_Title
#         self.Notes = Notes
#         print("checking")
#     def add_info(self):
#         print(self.name)


# address_book = student("s","a","s","a","s","a","s","s")
# address_book.add_info()

# Add new user contacts - step 1


# user_name = input("Please could you tell us your name")

# the next step would that it will check that is their name exists in database or not






add_user = insert_user_in_table("Agha Muhammad",'Imran', "07479963321")
print(add_user)

check_inserted_data = verfy_data_in_table()
print(check_inserted_data)

retreave_certain_data("Agha Muhammad",'Imran')






