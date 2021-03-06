#recordManager.py
#A program that allows a user to create new students 
# and to view students in a record
#Author: Shane Austin

def menu ():
    print("What would you like to do")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type on letter (a/v/q):").strip()
    
    return choice
#test the function
#choice = menu()
#print("you chose {}".format(choice))

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("enter name :")
    currentStudent["modules"] = readModules ()

    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit:").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\t\tEnter grade:"))
        modules.append(module)
        moduleName = input("\tEnter next module name (blank to quit:").strip()
    return modules

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        viewModules(currentStudent["modules"])

def viewModules(modules):
    print ("\tName \tGrade")
    for module in modules:
        print("\t{} \t{}".format(module["name"], module["grade"]))

#main program

students = []
choice = menu()
while (choice != "q"):

    if choice == "a":
        doAdd(students)
    elif choice == "v":
        doView(students)
    elif choice != "q":
        print("\n\n Please selecet either a, v or q")
    choice = menu()
