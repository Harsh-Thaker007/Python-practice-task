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

    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].roll_no == rn):
                return i
            
    def delete(self,rn):
        rn = int(input("Enter the roll_no to delte:"))
        i = obj.search(rn)
        del ls[i]    

ls = []
obj = Student('', 0, '')

# ch = int(input("Enter the choice:"))
while(True):

    print("\nEnter any one option:")
    print("\n 1.Accept \n 2.Display \n 3.Search \n 4.Delete \n 5.Exit")

    ch = int(input("\nEnter the choice:"))

    if (ch == 1):
        name =input("\nEnter name:")
        roll_no = int(input("Enter Roll_no:"))
        Address = input("Enter Address:")
        obj.accpet(name, roll_no,Address)

    elif (ch == 2):
        print("\n list of students:\n")
        for i in range(ls.__len__()):
            obj.display(ls[i])
    
    elif (ch == 3):
        rn = int(input("Enter Roll_no:"))
        if(rn == roll_no):
             print("\n Student Found, ")
             s = obj.search(rn)
             obj.display(ls[s])        
        else:
            print("Wrong Roll Number")


    elif (ch == 4):
        # d = obj.delete(rn)
        print(ls.__len__())
        print("List after deletion")
        for d in range(ls.__len__()):
            obj.display(ls[d])

    elif (ch == 5):
        break   