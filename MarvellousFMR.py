

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

def reduceX(Task, Elements):
    Sum=0

    for no in Elements:
        Sum=Task(Sum,no)

    return Sum