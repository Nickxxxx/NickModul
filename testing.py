
import logging



'''
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
'''

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


'''
class Car:

    def decide(self, method):
        if method == 'testlogger':
            Car.Audi('TestLog')
        elif method == 'testwarning':
            Car.motor('This is a warning')

    def Audi(self, name):
        self.h1_logger = logging.getLogger(name)
        return self.h1_logger
        
    def motor(self, msg):
        self.h1_logger.warning(msg)


class BMW:
        print("Test1")
        def msport(self):
            print("Test2")
            self.price_total = self.price1 *100
            print(f"This is a new M-Modell with a toalprice of {self.price_total} $")


Car = Car()
print("----------------------")

Car.decide('testlogger')
print("_________________")
Car.decide('testwarning')

print("----------------------")
'''

arguments = [{'test':'something'}]
print(arguments)
print(arguments[0])


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


