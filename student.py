class Student:

    def __init__(self, name, roll_no, address):
        self.name = name
        self.roll_no = roll_no
        self.address = address

    def accpet(self, Name, Roll_no, Address):
        ob = Student(Name, Roll_no, Address)
        ls.append(ob)

    def display(self, ob):
        print("Name:", ob.name)
        print("Roll No:", ob.roll_no)
        print("Address:", ob.address)


ls = []
obj = Student('', 0, '')

# ch = int(input("Enter the choice:"))
while(True):

    print("\nEnter any one option:")
    print("\n 1.Accept \n 2.Display \n 3.Exit")

    ch = int(input("\nEnter the choice:"))

    if (ch == 1):
        name =input("\nEnter name:")
        roll_no = int(input("Enter Roll_no:"))
        Address = input("Enter Address:")
        obj.accpet(name, roll_no,Address)

    elif (ch == 2):
        print("\n list of students: \n")
        for i in range(ls.__len__()):
            obj.display(ls[i])
    
    elif (ch == 3):
        break