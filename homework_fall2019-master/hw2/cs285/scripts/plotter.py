import csv

data_root_dir = "/Users/danielmeans/Projects/berkeleydeeprl/homework_fall2019-master/hw2/cs285/data/"

class Plotter:
    def __init__(self):
        pass

    def import_data(filename):
        filepath = data_root_dir + filename
        returns = []
        with open(filepath) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                val = row[2]
                if Plotter.isFloat(val):
                    returns.append(float(val))
        return returns[1:]
