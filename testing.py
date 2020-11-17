
import logging

logging.Formatter.formatMessage

print("------------------------------------------")


class Car:
    def Audi(self, *args, **kwargs):
        print(kwargs)
        print(args)
        y = [args, kwargs]
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


logging.basicConfig(format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Admin logged out')


logger = logging.getLogger('TestingLogger')
print(type(logger))
logger.basicConfig(format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
print(type(logger.basicConfig(
    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')))
logger.warning('Admin logged out')
print(type(logger.warning('Admin logged out')))

print("_______________________________________")

print(logging.Handler())

