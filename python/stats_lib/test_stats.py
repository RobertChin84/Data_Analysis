import statistics as stat
import csv
def get_data(filename):
    x = []
    y = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            x.append(float(row[1]))
            y.append(float(row[2]))
    return x,y
x,y = get_data('../../data/football.csv')
print stat.correlation(x,y,"population")