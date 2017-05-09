import pylab
from mpl_toolkits.mplot3d import Axes3D
import function
import numpy
# compute values 3D chart
def makeData():
    x = numpy.arange(-10, 10, 0.1)
    y = numpy.arange(-10, 10, 0.1)
    xgrid, ygrid = numpy.meshgrid(x, y)
    zgrid = function.Calculator().getSquareError(x, y)
    return xgrid, ygrid, zgrid


# create 3D chart
x, y, z = makeData()
fig = pylab.figure()
axes = Axes3D(fig)
axes.plot_surface(x, y, z)
axes.text3D(5, 10, 20, r'$3D\ chart$')
axes.set_xlabel(r'$intercept$')
axes.set_ylabel(r'$Slope$')
axes.set_zlabel(r'$Error$')
pylab.show()