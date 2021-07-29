from graphs.plotfile import Plotter

app = Plotter(xval=range(0,10), yval=range(0,10))
plot = app.plotthing()
#plot.show()
plot.savefig("./static/images/plot.png")