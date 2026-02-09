#Functional

# def CheckEven(No):
#     return(No%2==0)

CheckEven=lambda No:(No%2==0)

def main():
    Value=0
    Ret=False

    print("Enter number :")
    Value=int(input())

    Ret=CheckEven(Value)
    
    if (Ret==True):
        print("it is even")
    else:
        print("it is odd")

if __name__=="__main__":
    main()  