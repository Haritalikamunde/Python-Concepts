class Demo:
    No=10

    def __init__(self,A,B):
        self.Value1=A
        self.Value2=B

    def fun(self):
        print("Inside instance method fun : ",self.Value1, self.Value2)

    @classmethod
    def Sun(cls):
        print("Inside class method sun : ",cls.No)

Demo.Sun()
print("class variable No:", Demo.No)

obj=Demo(11,21)

obj.fun()
print("instance variable:",obj.Value1,obj.Value2)