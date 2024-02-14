import os
import sys

count = 0
def portfolio_cost(filename):
    count = 0.0
    with open(filename, 'r') as f:
        for line in f:
            try:
                line = line.split(" ")
                price = float(line[1])
                cost = float(line[2])
                count += price*cost
            except ValueError as e:
                print(e, "not number")
    return count



print(portfolio_cost('Data/portfolio3.dat'))