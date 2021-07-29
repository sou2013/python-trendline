# plotfile.py
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, xval=None, yval=None):
        self.xval = xval
        self.yval = yval

    def plotthing(self):
        f = plt.figure()
        sp = f.add_subplot(111)
        sp.plot(self.xval, self.yval, 'o-')
        return plt