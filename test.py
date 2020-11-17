
from SVLog import NickModul

def main(x, y):

    if y != 0:
        solution = x/y
        print(solution)
    else:
        logger = NickModul.getLogger('logger')

        print("------------------------------------------")


        NickModul.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
        NickModul.warning('Admin logged out')


main(10, 0)
