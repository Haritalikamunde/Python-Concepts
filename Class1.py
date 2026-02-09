class Demo:
    def __init__(self):
        print("Inside Constructor")

    def __del__(self):
        print("inside destructor")

obj=Demo()

print("End of application")