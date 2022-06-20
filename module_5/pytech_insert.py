from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.eur17uf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
students = client.pytech.get_collection("students")



students_insert = [
            { "student_id": 1007,
            "first_name": "Thorin",
            "last_name": "Oakenshield"},
            { "student_id": 1008,
            "first_name": "Bilbo",
            "last_name": "Baggins"},
            { "student_id": 1009,
            "first_name": "Frodo",
            "last_name": "Baggins"}
            ]
new_student_Id = students.insert_many(students_insert)
print("-- INSERT STATEMENTS --")
for student in students_insert:
    print("Inserted student record {} {} into the students collection with document_id {}".format(student["first_name"], student["last_name"], student["student_id"]))