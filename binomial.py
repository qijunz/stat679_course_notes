#!/usr/bin/env python3

""" function to calculate binomial coefficients """

import argparse
import math

# use an Argument Parser object to handle script arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="total number of items to choose from")
parser.add_argument("-k", type=int, help="number of items to choose")
parser.add_argument("-l", "--log", action="store_true", help="returns the log binomial coefficient")
parser.add_argument("--test", action="store_true", help="tests the module and quits")
args = parser.parse_args()

# test argument problems early:
if not args.test and __name__ == '__main__':
    # check input n, print warning if n is not be provided or not a positive integer
    if not args.n and (not type(args.n)==int):
        raise Exception("please provide -n")
    elif args.n<0 or not type(args.n)==int:
        raise Exception("argument -n must be positive integer")
    
    # check input k, print warning if k is not a positive integer
    if not args.k and (not type(args.k)==int):
        print("using default -k")
    elif args.k<0 or not type(args.k)==int:
        raise Exception("argument -k must be positive integer")

    # check if n is greater or equals to k
    if args.n < args.k:
        raise ValueError("n must be >=k")

def logfactorial(n, k=0):

    """function to calculate log(n!). examples:
    >>> logfactorial(5)
    4.787491742782046
    >>> logfactorial(5, k=3)
    2.995732273553991
    >>> logfactorial(5, k=5)
    0
    >>> logfactorial(5, k=6)
    Warning: n must be >=k
    """
    if n < k:
        return print("Warning: n must be >=k")
    
    log_result = 0

    for i in range(k, n):
        log_result += math.log(i+1)
    
    return log_result

def factorial(n):
    result = 1
    if n >0:
        for i in range(1, n+1):
            result *= i
    return int(result)

def choose(n,k=0,log=False):
    """returns the binomial coefficient. examples:
    >>> choose(5,3)
    10.0
    """
    if log:
        choose_return = logfactorial(n,k) - logfactorial((n-k))
    else:
        choose_return = factorial(n) / (factorial(k) * factorial((n-k)))
    return choose_return

def runTests():
    print("testing the module...")
    if args.n:
        print("ignoring n for the testing purpose")
    if args.k:
        print("ignoring k for the testing purpose")
    import doctest
    doctest.testmod()
    print("done with tests")

if __name__ == '__main__':
    if args.test:
        runTests()
    else:
        print(choose(args.n, args.k, args.log))
