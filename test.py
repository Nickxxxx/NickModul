
from SVLog import NickModul

def main1(x, y):

    if y != 0:
        solution = x/y
        print(solution)
    else:

        # create logger with 'spam_application'
        logger = NickModul.getLogger('spam_application')
        logger.setLevel(10)
        # create file handler which logs even debug messages
        fh = NickModul.FileHandler('spam.log')
        #fh.setLevel(10)
        # create console handler with a higher log level
        ch = NickModul.StreamHandler()
        #ch.setLevel(40)
        # create formatter and add it to the handlers 
        #fh.setFormatter(formatter)
        #ch.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)

        print("Test_1_")

        logger.info('creating an instance of auxiliary_module.Auxiliary')

        print("Test_2_")

        print("------------------------------------------")
        

def main2(x, y):

    if y != 0:
        solution = x/y
        print(solution)
    else:
        logger = NickModul.getLogger('testLogger')
        logger.warning('This is a Warning')
        logger.error("This is a legendary error")


def main3(x, y):

    if y != 0:
        solution = x/y
        print(solution)
    else:
        fh = NickModul.FileHandler('spam2.log')
        print(fh)
        fh.setLevel(10)


main2(10,0)



