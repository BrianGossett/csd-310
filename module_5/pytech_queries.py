from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.eur17uf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
students_doc = client.pytech.get_collection("students")
students = students_doc.find({})
found_student = students_doc.find_one({"student_id": 1007})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students:
    print("Student ID: {}".format(student["student_id"]))
    print("First Name: {}".format(student["first_name"]))
    print("Last Name: {}\n".format(student["last_name"]))

print("-- DISPLAYING STUDENT DOCUMENT FROM find one() QUERY --")
print("Student ID: {}".format(found_student["student_id"]))
print("First Name: {}".format(found_student["first_name"]))
print("Last Name: {}\n".format(found_student["last_name"]))