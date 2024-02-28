import csv

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares = self.shares - amount

def read_portfolio(filename):
    port = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            st = Stock(row[0], int(row[1]), float(row[2]))
            port.append(st)
    return port

def print_portfolio(port):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print("---------- ---------- ----------")
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
portfolio = read_portfolio('Data/portfolio.csv')
print_portfolio(portfolio)

