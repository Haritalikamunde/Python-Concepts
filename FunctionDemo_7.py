# Accept : Multiple parameters
# Return : One Value
def Demo(Value1, Value2):
    print("Inside Demo :", Value1, Value2)
    return 11

def main():
    Result = None
    Result = Demo("Python",21)
    print("return value is:", Result)


if __name__=="__main__":
    main()