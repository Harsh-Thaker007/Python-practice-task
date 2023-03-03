from dataclasses import dataclass

@dataclass
class Student:
    name: str
    roll_no: int
    address: str

    # def __init__(self, name, roll_no, address):
    #     self.name = name
    #     self.roll_no = roll_no
    #     self.address = address

    def accpet(self, Name, Roll_no, Address):
        ob = Student(Name, Roll_no, Address)
        ls.append(ob)

    def display(self, ob):
        print("Name:", ob.name)
        print("Roll No:", ob.roll_no)
        print("Address:", ob.address)
        print("\n")

    def search(self, rn):
        for i in range(ls.__len__()):
           if(ls[i].roll_no == rn):
               return i
            
            
    def delete(self,rn):
       
        i = obj.search(rn)
        del ls[i]    

    def update(self,rn,No): 
        i = obj.search(rn)
        roll = No 
        ls[i].roll_no = roll

ls = []
obj = Student('', 0, '')

# ch = int(input("Enter the choice:"))
print("---------WELCOME -------")
while(True):
   
    print("\nEnter any one option:")
    print("\n 1.Accept \n 2.Display \n 3.Search \n 4.Delete \n 5.Update \n 6.Exit")

    ch = int(input("\nEnter the choice:"))
    
    if (ch == 1):
        n = int(input("\nEnter the user u want:"))
        i = n
        while(i >= 1):        
            name =input("\nEnter name:")
            roll_no = int(input("Enter Roll_no:"))
            Address = input("Enter Address:")
            obj.accpet(name, roll_no,Address)
            i = i-1
  
    elif (ch == 2):
        if(ls.__len__() > 0):
            print("\n list of students:\n")
            for i in range(ls.__len__()):
             obj.display(ls[i])
        else:
            print("NO DATA INSERTED")

    elif (ch == 3):
        rn = int(input("Enter Roll_no:"))
        if([obj for obj in ls if obj.roll_no == rn]):
             print("\n Student Found, ")
             s = obj.search(rn)
             obj.display(ls[s])        
        else:
            print("Wrong Roll Number")


    elif (ch == 4):
        rn = int(input("Enter the roll_no to delte:"))
        d = obj.delete(rn)
        print(ls.__len__())
        print("List after deletion")
        for d in range(ls.__len__()):
            obj.display(ls[d])

    elif (ch == 5):
        rn = int(input("enter the number u want to update:"))
        roll =  int(input("enter the number u want to add:"))
        e = obj.update(rn,roll)
        print(ls.__len__())
        print("List after updation")
        for e in range(ls.__len__()):
            obj.display(ls[e])

    elif (ch == 6):
        break   