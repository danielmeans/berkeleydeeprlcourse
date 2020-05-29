import csv
from collections import namedtuple
import matplotlib.pyplot as plt
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

    def plot_learning_curves(self, save_plots=False):

        #large batch plot
        lb_runs = ['lb_rtg_dsa', 'lb_rtg_na', 'lb_no_rtg_dsa']
        for lb_run in lb_runs:
            y = getattr(self.eval_returns, lb_run)
            x = [iter for iter in range(len(y))]
            plt.plot(x, y, label=lb_run)
        plt.xlabel('Iteration')
        plt.ylabel('Average Return')
        plt.legend()
        if save_plots:
            plot_name = 'lb_average_returns.png'
            plt.savefig(data_root_dir + plot_name)
        plt.show()

        #Small batch plot
        sb_runs = ['sb_rtg_dsa', 'sb_rtg_na', 'sb_no_rtg_dsa',]
        for sb_run in sb_runs:
            y = getattr(self.eval_returns, sb_run)
            x = [iter for iter in range(len(y))]
            plt.plot(x, y, label=sb_run)
        plt.xlabel('Iteration')
        plt.ylabel('Average Return')
        plt.legend()
        if save_plots:
            plot_name = 'sb_average_returns.png'
            plt.savefig(data_root_dir + plot_name)
        plt.show()

    def isFloat(str):
        try:
            float(str)
            return True
        except ValueError:
            return False

def main():
    plotty = Plotter()
    plotty.plot_learning_curves(save_plots=True)
if __name__ == '__main__':
    main()
