def add(*val):
    sums = 0
    for n in val:
        sums += n
    return sums

print(add(5,6,7,8))

def calculate(n,**kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)


calculate(2,add=3, multiply=5)

class Car:
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("colour")


my_car = Car(make="Nissan")
print(my_car.model)
