import predicates
import generators

from strategies.selection_sort_strategy import SelectionSortStrategy
from strategies.bubble_sort_strategy import BubbleSortStrategy
from strategies.insertion_sort_strategy import InsertionSortStrategy


def sameTypefunc(n):
    return n


def main():

    strategy = InsertionSortStrategy(lambda x: x, predicates.intAsc)

    nums = generators.ints(0,100,10)
    print(nums)

    print(strategy.sort(nums))
    print(strategy.get_result(len(nums)))
    #print(strategy.get_result(len(nums)))




if __name__ == '__main__':
    main()
