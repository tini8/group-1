from typing import Iterable


def replace_first(items: list) -> Iterable:
    
    return items[3:len(items):] + items[0:3]
    return remove.items[1] 


if __name__ == '__main__':
    x = input("input 4 numbers or letters:  ")
    
    print(list(replace_first(x)))

