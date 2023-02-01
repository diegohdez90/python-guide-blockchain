import math

numbers = [5, 6, 5, 6, 7, 5, 5, 2, 3, 4, 1,
           4, 1, 4, 6, 7, 8, 5, 3, 2, 4, 7, 5, 6, 3]


def lambda_method(numbers, **keyword_args):
    method_arg = keyword_args['method']
    for n in numbers:
        print(method_arg(n))


lambda_method(
    numbers, method=lambda n: "{:>20.6f} meters squared".format(math.pi * n**2))
