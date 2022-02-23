import itertools
from typing import Tuple, TypeVar, Iterable

T = TypeVar('T')

def groupby_index(iter: Iterable[T],n:int) -> Iterable[Iterable[T]]:
    """group list by index

    Args:
        iter (Iterable[T]): iterator to group by index
        n (int): The size of groups

    Returns:
        Iterable[Iterable[T]]: iterable object to group by index

    >>> [*map(lambda x:[*x],groupby_index([1,2,3,4],2))]
    [[1, 2], [3, 4]]
    """
    def keyfunc(x: Tuple[int,T]) -> int:
        k, _ = x
        return (k // n)
    def mapper(x: Tuple[int, Tuple[int, T]]):
        _, v = x
        return map(lambda y: y[1],v)
    g = itertools.groupby(enumerate(iter), keyfunc)
    return map(mapper,g)

if __name__ == "__main__":
    test_list = [*range(20,-10,-1)]
    for g in groupby_index(test_list,4):
        print([*g])
    print("===")
    print([*map(lambda x:[*x],groupby_index([1,2,3,4],2))])
    for g in groupby_index([1,2,3,4],2):
        print([*g])
    