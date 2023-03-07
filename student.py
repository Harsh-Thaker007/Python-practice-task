from dataclasses import dataclass

@dataclass
class Student:
    name: str
    roll_no: int
    address: str

    # def __inselit__(self, name, roll_no, address):
    #     f.name = name
    #     self.roll_no = roll_no
    #     self.address = address

    # dict = {}

    # def standard(self):
    #     q = int(input("Enter the class u want:"))


    def accpet(self, Name, Roll_no, Address,cl,d):
        ob = Student(Name, Roll_no, Address)
        
        # d[cl] = []
        d[cl].append(ob)
        print(cl)
        print(d)

    def display(self, ob):
        print("Name:", ob.name)
        print("Roll No:", ob.roll_no)
        print("Address:", ob.address)   
        print("\n")

    def search(self, rn,cl,d):
        print(cl)
        print(d[cl])
        print(int(len(d[cl])))
        for i in range(len(d[cl])):
            print(d[cl][i])
            if(d[cl][i].roll_no == rn):
               
               return i
            
            
    def delete(self,rn,d,cl):
       
        i = self.search(rn,cl,d)
        print(i)
        d[cl].pop(i)

    def update(self,rn,No,d,cl): 
        i = obj.search(rn,cl,d)
        roll = No 
        d[cl][i].roll_no = roll

    def register(self,cl):
    #    cl = int(input("Enter the clas (1 to 4):"))
       if (cl==1 or cl==2 or cl==3 or cl==4):       
          True
       else:
           print("Entered wrong class")
           exit()

# d = dict.fromkeys([1,2,3,4],[])


ls = []

obj = Student('', 0, '')

print("---------WELCOME -------")
def whole():
  d={dict_lst : [] for dict_lst in range(1,5) } 
  while(True):
    
    cl = int(input("Enter the class (1 to 4):"))
    obj.register(cl)

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
            obj.accpet(name, roll_no,Address,cl,d)
            i = i-1
  
    elif (ch == 2):
            if(len(d) > 0):
                print("\n list of students:\n")
                for i in range(len(d[cl])):
                 obj.display(d[cl][i])
            else:
                print("NO DATA INSERTED")

    elif (ch == 3):
        rn = int(input("Enter Roll_no:"))
        if([obj for obj in d[cl] if obj.roll_no == rn]):
             print("\n Student Found, ")
             s = obj.search(rn,cl,d)
             obj.display(d[cl][s])        
        else:
            print("Wrong Roll Number")


    elif (ch == 4):
        rn = int(input("Enter the roll_no to delte:"))
        q = obj.delete(rn,d,cl)
        print(len(d[cl]))
        print("List after deletion")
        for q in range(len(d[cl])):
            obj.display(d[cl][q])

    elif (ch == 5):
        rn = int(input("enter the number u want to update:"))
        roll =  int(input("enter the number u want to add:"))
        e = obj.update(rn,roll,d,cl)
        print(len(d[cl]))
        print("List after updation")
        for e in range(len(d[cl])):
            obj.display(d[cl][e])

    elif (ch == 6):
        break   

whole()
