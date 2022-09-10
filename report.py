from strategies.abstract_strategy import AbstractStrategy
from strategies.bubble_sort_strategy import BubbleSortStrategy
from strategies.insertion_sort_strategy import InsertionSortStrategy
from strategies.selection_sort_strategy import SelectionSortStrategy
from strategies.merge_sort_strategy import MergeSortStrategy
from strategies.quick_sort_strategy import QuickSortStrategy
from models.run_result import RunResult

import generators
import predicates

import pandas as pd

def generate_nums() -> list[list[int]]:

    top_list = []

    starting_size = 2
    stopping_size = 300
    step = 1    

    for i in range(starting_size,stopping_size+1,step):
        nums = generators.ints(-10000,100000,i)
        top_list.append(nums)

    return top_list

def strategy_list() -> list[AbstractStrategy]:
    strategies = []
    simple_map = lambda x: x

    strategies.append(BubbleSortStrategy(simple_map,predicates.intAsc))
    strategies.append(SelectionSortStrategy(simple_map,predicates.intAsc))
    strategies.append(InsertionSortStrategy(simple_map,predicates.intAsc))
    strategies.append(MergeSortStrategy(simple_map,predicates.intAsc))
    strategies.append(QuickSortStrategy(simple_map,predicates.intAsc))

    return strategies

def run_strategies(nums: list[list[int]],strategies: list[AbstractStrategy]):

    results : list[RunResult] = []

    for strategy in strategies:
        for int_set in nums:

            print("{}: {}".format(strategy._strategy_name,len(int_set)))

            strategy.clear_statistics()
            strategy.sort(int_set)

            result = strategy.get_result(len(int_set)).to_tuple()
            results.append(result)

    return results

def main():

    nums = generate_nums()
    strategies = strategy_list()
    results = run_strategies(nums,strategies)

    df = pd.DataFrame.from_records(results,columns=RunResult.short_labels())
    df['total'] = df['reads'] + df['writes'] + df['comparisons']

    df.to_csv('sorting.csv',index=False)


if __name__ == "__main__":
    main()