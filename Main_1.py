def Multiplication(Value1,Value2):
    Ans=0
    Ans=Value1*Value2
    return Ans

print("Demo application")

def main():
    No1=0
    No2=0
    result=0

    No1=int(input("Enter first number :"))
    No2=int(input("Enter second number :"))

    result=Multiplication(No1,No2)
    print("multiplication is :", result)


main()
