import logging

print(logging.getLoggerClass)

print(logging.setLoggerClass)


logging.getLogRecordFactory()
logging.getLoggerClass()

print("------------------------------------------")

class Car:
    def Audi(self, *args, **kwargs):
        print(kwargs)
        print(args)
        y =  [args , kwargs]
        print(y)

car = Car()
car.Audi(10, 3445, marke="Audi", art="Q3", leistung="180PS")

y = (23, 4332)
z = {'marke': 'BMW', 'art': 'X3', 'leistung': '160PS'}
car.Audi(*y, **z)


print(" heeeeelllllllloooooo  ")

if logging.raiseExceptions:
    print("hello")
else:
    print("he")

test = logging.getLogger('TestingLogger')
test.warning("This is a test")
print(test)

logging.basicConfig()

print(logging.BufferingFormatter)

