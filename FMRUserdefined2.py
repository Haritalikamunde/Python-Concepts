# user defined Map

from functools import reduce

CheckEven=lambda No:(No%2==0)

Increment=lambda No:No+1

Add=lambda A,B:(A+B)

def filterX(task,Elements):
    Result=list()

    for no in Elements:
        Ret=task(no)

        if( Ret== True):
            Result.append(no)

    return Result

def MapX(task, Elements):
    Result=list()

    for no in Elements:
        Ret=task(no)
        Result.append(Ret)

    return Result

def main():
    Data=[11,10,15,20,22,27,30]
    print("Actual Data is :",Data)

    FData=list(filterX(CheckEven,Data))

    print("Data after filter is :", FData)

    MData=list(MapX(Increment,FData))

    print("Data after map is :", MData)

    RData=reduce(Add,MData)

    print("Data after reduce is :", RData)

if __name__=="__main__":
    main()