
import logging


# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam2.log')
print(fh)
#fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
#ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
# add the handlers to the logger
logger.addHandler(fh)
print(logger)
logger.addHandler(ch)

logger.info('creating an instance of auxiliary_module.Auxiliary')

print('__________________________________________________')


print("test1")
print("-----")
print("test2")
print("-----")
h1_getLogger = logging.getLogger('Test')
print("test3")
print(h1_getLogger)
print("-----")
print("test4")
print(type(h1_getLogger))
print("-----")

print('___________________________________________________')

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
LoggingNick.data('logger.warning')


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


