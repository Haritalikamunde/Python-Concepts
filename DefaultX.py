
def EmployeeInfo(Name,Age,Salary,City="Pune"):
    print("Name :",Name)
    print("Age :", Age)
    print("Salary :", Salary)
    print("City :",City)

def main():
    EmployeeInfo("rahul",50,2000.20)                  
    EmployeeInfo("rahul",50,2000.20,"Mumbai")

if __name__=="__main__":
    main()