
import logging


logging.Template('template')


print('_______________________________________________________---')

class LogginNick:
    def data(self, method):
        method = method

        global h1
        if method == 'getLogger':
            name = 'Test'
            h1 = logging.getLogger(name)
            print(h1)
        
        elif method == 'logger.warning':
            h1.warning("This is a logging message")
        
        elif method == 'logger.debug':
            h1.debug("This is a debug Log")
        
        else:
            pass


LoggingNick = LogginNick()
print(type(LoggingNick.data('getLogger')))
#LoggingNick.data('logger.warning')


h1 = logging.getLogger("Test")
h1.warning("This is log test warning")


print("------------------------------------------")


class Car:
    def Audi(self, *args, **kwargs):
        print(kwargs)
        print(args)
        y = [args, kwargs]
        print(y)

    def engine(self, Ps):
        power = Ps
        return power

    class BMW:
        def msport(price):
            print(f"This is a new M-Modell with a price of {price} $")

'''

class Auto(Car):
    def newengine(self, newPs):
        x = Car.engine + newPs
        print(x)





car = Car()
car.engine(150)

Auto = Auto()
Auto.newengine(100)

'''

print("------------------------------------------")

y = (23, 4332)
z = {'marke': 'BMW', 'art': 'X3', 'leistung': '160PS'}
#car.Audi(*y, **z)


print(" heeeeelllllllloooooo  ")

if logging.raiseExceptions:
    print("hello")
else:
    print("he")


print("_______________________________________")

logging.Logger.warning("This is a warning")

