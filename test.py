
from SVLog import NickModul

def main1():
    # create logger with 'spam_application'
    logger1 = NickModul.getLogger('spam_application')
    logger1.setLevel(10)
    fg = NickModul.FileHandler('Spam2.log')
    fg.setLevel(10)
    ch = NickModul.StreamHandler()
    ch.setLevel(10)
    logger1.addHandler(ch)
    logger1.addHandler(fg)

    logger1.error('creating an instance of auxiliary_module.Auxiliaryfor Test1')
    #------------------------------------------

    # create another logger with 'spam_application2'
    logger2 = NickModul.getLogger('spam_application2')
    logger2.setLevel(10)
    fg = NickModul.FileHandler('Spam1.log')
    fg.setLevel(10)
    ch = NickModul.StreamHandler()
    ch.setLevel(10)
    logger2.addHandler(ch)
    logger2.addHandler(fg)

    logger2.error('creating an instance of auxiliary_module.Auxiliary for Test2')

#main1()

############################################################

def main2():
    NickModul.basicConfig(format='%(asctime)s %(message)s')
    NickModul.warning('is when this event was logged.')

    #this should overwrite the logging basicConfig
    NickModul.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    NickModul.warning('is when this event was logged.')

#main2()

############################################################

def main3():
    #Testing different logging methods
    NickModul.debug('This is a debug message')
    NickModul.info('This is an info message')
    NickModul.warning('This is a warning message')
    NickModul.error('This is an error message')
    NickModul.critical('This is a critical message')
    

#main3()

############################################################

def main4():
    logger = NickModul.getLogger('simple_example')

    logger.setLevel(10)
    #logger.setLevel(NickModul.DEBUG)  <-- diese Variante funktioniert noch nicht

    # create console handler and set level to debug
    ch = NickModul.StreamHandler()
    ch.setLevel(10)

    # create formatter and add it to handler/logger
    formatter = NickModul.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

main4()

def main5():
    NickModul.config.fileConfig(fname='file.conf', disable_existing_loggers=False)
    # create logger
    logger = NickModul.getLogger('simpleExample')

    # 'application' code
    logger.debug('debug message')

main5()
