# Accept : Multiple parameters
# Return : Multiple Value
def Demo(Value1, Value2):
    print("Inside Demo :", Value1, Value2)
    return 11,21,31

def main():
    Result1 = None
    Result2 = None
    Result3 = None
    Result1, Result2, Result3 = Demo("Python",21)
    print("return value are:", Result1, Result2, Result3)


if __name__=="__main__":
    main()