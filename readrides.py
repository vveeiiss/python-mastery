# readrides.py
from collections import namedtuple
import collections
import csv

class Row1:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

class Row2:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

Row3 = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

def read_rides_as_tuples(filename, dtype = "tuple"):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            if dtype == "tuple":
                record = (route, date, daytype, rides)
                records.append(record)
            if dtype == "class":
                records = Row1(route, date, daytype, rides)
            if dtype == "class_slots":
                records = Row2(route, date, daytype, rides)
            if dtype == "num":
                records = Row3(route, date, daytype, rides)
    return records


def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides' : rides
                }
            records.append(record)
    return records


class RideData(collections.abc.Sequence):
    def __init__(self):
        self.routes = []      # Columns
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        return {'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    records = RideData()
    rows = read_rides_as_tuples('Data/ctabus.csv', "num")
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
