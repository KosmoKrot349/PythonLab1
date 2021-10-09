class Animal:
    __slots__ = ('count','weight','height','classification')

    def __del__(self):
        print('i have deleted animal object')
        Animal.count-=1

    def __init__(self,  weight=0, height=0, classification=""):
        Animal.count+=1
        self.height = height
        self.weight = weight
        self.classification = classification

    def setWeight(self,weight):
        self.weight=weight

    def getWeight(self):
        return self.weight

    def setHieght(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def setClass(self, classification):
        self.classification = classification

    def getClass(self):
        return self.classification

    def input(self):
        self.weight=float(input("Enter weight: \n"))
        self.height = float(input("Enter height: \n"))
        self.classification=str(input("Enter class: \n"))

    def show(self):
        return F'Animal weight:{self.weight},height:{self.height},classification:{self.classification}'

class Pet(Animal):
    __slots__ = ('sound','food')

    def input(self):
        super().input()
        self.sound = str(input("Enter sound: \n"))
        self.food = str(input("Enter food: \n"))

    def setSound(self, sound):
        self.sound = sound

    def getSound(self):
        return self.sound

    def setFood(self, food):
        self.food = food

    def getFood(self):
        return self.food

    def __del__(self):
        print('i have deleted pet')

    def __init__(self,  weight=0, height=0, classification="",sound="", food=""):
        super().__init__(weight, height, classification)
        self.sound = sound
        self.food = food

    def show(self):
        return super().show()+F',sound:{self.sound} food:{self.food}'

class Cow(Pet):
    __slots__ = ('name','age')

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def __del__(self):
        print('i have deleted cow')

    def __init__(self, weight=0, height=0, classification="", sound="", food="", name="", age=0):
        super().__init__(weight, height, classification,sound,food)
        self.name = name
        self.age = age

    def input(self):
        super().input()
        self.name = str(input("Enter name \n"))
        self.age = int(input("Enter age \n"))

    def show(self):
        return super().show() + F',name:{self.name} age:{self.age}'

if __name__ == "__main__":
    var1 = Cow(1,2,'someClass1','someSound1','someFood1','someName1', 213)
    var2 = Cow(3,4,'someClass2','someSound2', 'someFood2', 'someName2', 21)
    var3 = Cow()
    var3.input()
    print(var1.show())
    print(var2.show())
    print(var3.show())
