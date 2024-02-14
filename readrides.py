# readrides.py
from collections import namedtuple
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

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_tuples('Data/ctabus.csv', "num")
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
