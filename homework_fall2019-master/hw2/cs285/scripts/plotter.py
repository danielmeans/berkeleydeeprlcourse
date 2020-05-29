import csv
from collections import namedtuple

data_root_dir = "/Users/danielmeans/Projects/berkeleydeeprl/homework_fall2019-master/hw2/cs285/data/"

class Plotter:
    def __init__(self):
        self.runs = ['lb_rtg_dsa', 'lb_rtg_na', 'lb_no_rtg_dsa', 'sb_rtg_dsa', 'sb_rtg_na', 'sb_no_rtg_dsa', ]
        EvalReturns = namedtuple('EvalReturns', self.runs)
        self.eval_returns =EvalReturns
        for run in self.runs:
            self.import_data(run)

    def import_data(self, filename):
        filepath = data_root_dir + filename + '.csv'
        returns = []
        with open(filepath) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                val = row[2]
                if Plotter.isFloat(val):
                    returns.append(float(val))
        setattr(self.eval_returns, filename, returns)

    def isFloat(str):
        try:
            float(str)
            return True
        except ValueError:
            return False

def main():
    plotty = Plotter()
    for run in plotty.runs:
        print(getattr(plotty.eval_returns, run))
if __name__ == '__main__':
    main()
