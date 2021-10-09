class Animal:

    __slots__ = ('weight','height','classification')
    count = 0

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
        Animal.input(self)
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

    def __init__(self,  weight=0, height=0, classification="",sound="", food=""):
        Animal.__init__(self,weight, height, classification)
        self.sound = sound
        self.food = food

    def show(self):
        return Animal.show(self)+F',sound:{self.sound} food:{self.food}'

class Dog(Pet):
    __slots__ = ('name', 'age')


    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age


    def __init__(self, weight=0, height=0, classification="", sound="", food="", name="", age=0):
        Pet.__init__(self, weight, height, classification,sound,food)
        self.name = name
        self.age = age

    def input(self):
        Pet.input(self)
        self.name = str(input("Enter name \n"))
        self.age = int(input("Enter age \n"))

    def show(self):
        return Pet.show(self) + F',name:{self.name} age:{self.age}'



class Pack:

    dogs = list()


    def addNewDog(self, dog):
        self.dogs.append(dog)

    def removeLastDog(self):
        self.dogs.pop()

    def showPack(self):
        for dog in pack.dogs:
            print(dog.show())

    def sortPack(self, parametr):

        if parametr == 'weight':
            self.dogs.sort(key=lambda x: x.weight)
        if parametr == 'height':
            self.dogs.sort(key=lambda x: x.height)
        if parametr == 'classification':
            self.dogs.sort(key=lambda x: x.classification)
        if parametr == 'name':
            self.dogs.sort(key=lambda x: x.name)
        if parametr == 'sound':
            self.dogs.sort(key=lambda x: x.sound)
        if parametr == 'food':
            self.dogs.sort(key=lambda x: x.food)









if __name__ == "__main__":
    var1 = Dog(3,2,'someClass1','someSound1','someFood1','someName1', 213)
    var2 = Dog(1,1,'someClass2','someSound2', 'someFood2', 'someName2', 21)
    pack = Pack()

    pack.addNewDog(var1)
    pack.addNewDog(var2)
    pack.showPack()

    pack.removeLastDog()
    pack.showPack()

    pack.sortPack('weight')
    pack.showPack()







