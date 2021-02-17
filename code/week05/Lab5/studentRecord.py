#studentRecord.py
#A program that stores and prints student data
#Shane Austin

student = {
    "name": "Mary",
    "courses": [
        { 
            "subject" : "Programming",
            "grade" : 45
        },

        {
            "subject" : "History",
            "grade" : 99
        }
    ]
}

print ("Student: {}".format(student["name"]))
for course in student["courses"]:
    print("\t {} \t: {}".format(course["subject"], course["grade"]))