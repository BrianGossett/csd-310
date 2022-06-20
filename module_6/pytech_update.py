# Brian Thomas Gossett
# June 20 2022
# Week 5 module 6.2
# Updating MongoDB

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.eur17uf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
students = client.pytech.get_collection("students")

students_list = students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students_list:
    print("Student ID: {}".format(student["student_id"]))
    print("First Name: {}".format(student["first_name"]))
    print("Last Name: {}\n".format(student["last_name"]))

result = students.update_one({"student_id": 1007}, {"$set": {"last_name": "Smith"}})

found_student = students.find_one({"student_id": 1007})

print("-- DISPLAYING STUDENT DOCUMENT FROM find one() QUERY --")
print("Student ID: {}".format(found_student["student_id"]))
print("First Name: {}".format(found_student["first_name"]))
print("Last Name: {}\n".format(found_student["last_name"]))

input("\n\nEnd of program, press any key to continue...")