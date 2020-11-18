
from SVLog import NickModul

def main(x, y):

    if y != 0:
        solution = x/y
        print(solution)
    else:
        logger = NickModul.getLogger("Logger")
        
        logger.warning("This is a new logge warning")
        

        print("------------------------------------------")
        



main(10, 0)
