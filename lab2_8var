class Pupil:
    count=0
    __name=""
    __age=0
    __class=""

    def __init__ (self):
        Pupil.count+=1
        print(Pupil.count)

    def __init__ (self,nm="",ag=0,cl=""):
        Pupil.count+=1
        print(Pupil.count)
        try:
            self.__name=nm
            self.__age=ag
            self.__class=cl
        except ValueError as e:
            print (e)

    def set_name(self, nm):
        self.__name=nm

    def set_age(self, ag):
        self.__age=ag

    def set_class(self, cl):
        self.__class=cl

    def get_class(self):
        return self.__name

    def get_class(self):
        return self.__age

    def get_class(self):
        return self.__class

    def read(self):
        try:
            self.__name=str(input("Enter name: \n"))
            self.__age=int(input("Enter age \n"))
            self.__class=str(input("Enter class\n"))
        except ValueError:
            print("Error")

    def show(self):
        print(f"Name {self.__name} Age {self.__age} Class {self.__class}")

if __name__ == "__main__":
    var1 = Pupil()
    var2 = Pupil()
    var1.read()
    var2.read()
    var1.show()
    var2.show()
        
