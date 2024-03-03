import csv
import reader

class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)

    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares = self.shares - amount

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    def __repr__(self):
        return f'{type(self).__name__}({self.name!r}, {self.shares!r}, {self.price!r})'

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
    for s in port:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))


s = Stock("AB", 100, 100.0)
print(s.__repr__())
a = Stock('GOOG', 100, 490.1)
b = Stock('GOOG', 100, 490.1)
print(a == b)
portfolio = reader.read_csv_as_instances('Data/portfolio.csv', Stock)
#tableformat.print_table(portfolio, ['name','shares','price'])

