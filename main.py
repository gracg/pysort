import comparators
from strategies.BubbleSortStartegy import BubbleSortStrategy
from comparators import *

def sameTypefunc(n):
    return n

def main():
    strategy = BubbleSortStrategy(lambda x:x, comparators.intDes)

    l = [9,2,3,3,4,22,1,9999,223,1]

    print(strategy.sort(l))



if __name__ == '__main__':
    main()
