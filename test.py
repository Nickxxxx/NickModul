
from SVLog import NickModul

def main1(x, y):

    if y != 0:
        solution = x/y
        print(solution)
    else:

        # create logger with 'spam_application'
        logger1 = NickModul.getLogger('spam_application')
        logger1.setLevel(10)

        fg = NickModul.FileHandler('Spam2.log')
        fg.setLevel(10)

        ch = NickModul.StreamHandler()
        ch.setLevel(10)

        logger1.addHandler(ch)
        logger1.addHandler(fg)
        

        print("Test_1_")

        logger1.error('creating an instance of auxiliary_module.Auxiliaryfor test1')

        print("Test_2_")


        print("------------------------------------------")

        # create logger with 'spam_application'
        logger2 = NickModul.getLogger('spam_application2')
        logger2.setLevel(10)

        fg = NickModul.FileHandler('Spam1.log')
        fg.setLevel(10)

        ch = NickModul.StreamHandler()
        ch.setLevel(10)

        logger2.addHandler(ch)
        logger2.addHandler(fg)

        print("Test_1_")

        logger2.error('creating an instance of auxiliary_module.Auxiliary for Test2')

        print("Test_2_")


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


def main4(x, y):

    if y != 0:
        solution = x/y
        print(solution)
    else:
        NickModul.DEBUG()


main4(10,0)



