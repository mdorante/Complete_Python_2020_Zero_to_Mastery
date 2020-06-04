# Lambda Expressions: one-time anonymous functions that you only need once

# They look like this -> lambda (params): action(params)

# Let's turn all these functions into lambda expressions and apply them to the data set


from functools import reduce

my_list = [1, 2, 3]


def mult_by2(item):
    return item * 2


print(list(map(lambda item: item * 2, my_list)))  # [2, 4, 6]


def only_odd(item):
    return item % 2 != 0


print(list(filter(lambda item: item % 2 != 0, my_list)))  # [1, 3]


def accumulator(acc, item):
    return acc + item


print(reduce(lambda acc, item: acc + item, my_list))  # 6
