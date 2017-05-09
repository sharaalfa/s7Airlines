import index
import numpy
import random
import pandas
import function2
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# calculate values charts and errors
class Calculator:

    def getMinFunc2(self):
        function2.Determinator().createTemporaryFile('val')
        for b in range(-5, 5):
            for a in range(-100, 100):
                p = Calculator().getMinFunc(a, b)
                function2.Determinator.writeToFile(p)
                data = pandas.read_csv('temporary.csv')
        return min(data['val'].values)

    def funcXX(self, x):
        return Calculator().getSquareError(x[0], x[1])
    def getMinOfLBFGS(self):
        for i in range(1, 25000):
            a = index.data['Weight'].loc[i]
            b = index.data['Height'].loc[i]
            m = numpy.array([[a, a * a], [b, a]])
            v = numpy.array([a * b, b])
            p = numpy.linalg.solve(m, v)
            if float(-5) < round(p[1], 1) < float(5):
                if float(-100) < round(p[0], 1) < float(100):
                    x0 = [p[1], p[0]]
                    res = minimize(Calculator().funcXX, x0, method='L-BFGS-B')
                    return res.x[0], res.x[1]



    def getMin(self):
        func = function2.Determinator()
        func.createTemporaryFile('w1opt' + ',' + 'error')
        for i in range(1, 25000):
            w1 = (50 - index.data['Height'].loc[i])/index.data['Weight'].loc[i]
            if float(-5) < round(w1, 1) < float(5):
                error = Calculator().getSquareError(50, w1)
                func.writeToFile(str(w1) + ',' + str(error))
        values = pandas.read_csv('temporary.csv')
        values = pandas.DataFrame({'w1opt': values['w1opt'].values,
                                   'error': values['error'].values})

        for j in range(1, 25000):
            if values['error'].loc[j] == min(values['error']):
                return values['w1opt'].loc[j]





    def getScatter(self):
        return index.data[['Weight', 'Height']]\
            .plot(x='Weight', y='Height', kind='scatter')

    def getChart2(self):
        func = function2.Determinator()
        func.createTemporaryFile('w1')
        for i in range(1, 25000):
            w1 = numpy.array(random.random())
            func.writeToFile(w1)

        values = pandas.read_csv('temporary.csv')
        values = pandas.DataFrame({'w1': values['w1'].values})
        func.createTemporaryFile('values1')
        for i in range(1, 25000):
            w1 = values['w1'].loc[i]
            val = Calculator().getSquareError(50, w1)
            func.writeToFile(val)

        values1 = pandas.read_csv('temporary.csv')
        values1 = pandas.DataFrame(values1).values
        plt.plot(values['w1'].values, values1)
        plt.xlabel(r'$w1$')
        plt.ylabel(r'$Error\ amount$')
        plt.title(r'$Error\ curve$')
        plt.grid(True)
        plt.show()


    def getChart(self, w0, w1):
        Calculator().getScatter()
        plt.plot(index.data['Weight'].values,
                 pandas.DataFrame(map(lambda a: w0 - w1 * a,
                                      index.data['Weight'])).values)
        plt.xlabel(r'$Weight$')
        plt.ylabel(r'$Height$')
        plt.title(r'$Relations:weight&height$')
        plt.grid(True)
        plt.show()

    def getSquareError(self,w0, w1):
        self.w0 = w0,
        self.w1 = w1,
        sum = 0
        for value in range(1, 25000):
            error = map(lambda a: a*a, [
                (index.data['Height'].loc[value]
                 - (numpy.float64(self.w0)
                    + numpy.float64(self.w1)*index.data['Weight'].loc[value]))])
            sum += error.pop()
        return numpy.float64(sum)

#Calculator().getSquareError(50, 0.04)


# computes and function of projects
class Determinator:


    def createHist(self, v, n, v1, v2, v3, w, m, w1, w2, w3):

        # create height histogram
        plt.figure(1)
        plt.subplot(n)
        plt.title('Histograms height & weight')
        plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
        plt.hist(v, v1, normed=1, facecolor='g', alpha=0.75)
        plt.xlabel(v2)
        plt.ylabel('quantity')
        plt.axis([60, 75, 0, v3])
        plt.grid(True)

        # create weight histogram
        plt.subplot(m)
        plt.hist(w, w1, normed=1, facecolor='b', alpha=0.75)
        plt.xlabel(w2)
        plt.ylabel('quantity')
        plt.axis([78, 171, 0, w3])
        plt.grid(True)

        plt.show()

    def setValues(self, x):
        self.value=x
        return self.value




    def createPair(self, a, b, c):
        # create picture pair relation
        plt.plot(a, Determinator().setValues(c), b,
                 Determinator().setValues(a), b,
                 Determinator().setValues(c))
        plt.xlabel(r'$x$')
        plt.ylabel(r'$f(x)$')
        plt.title(r'$Relations:weight&BMI-blue,'
                  r'\ height&weight-green,\ height&BMI-red$')
        plt.grid(True)
        plt.show()


    def weight_category(self):
        function2.Determinator().createTemporaryFile('Weight_category')
        for i in index.data['Weight']:
            if i < 120:
                function2.Determinator().writeToFile('1')
            elif i >= 150:
                function2.Determinator().writeToFile('3')
            else:
                function2.Determinator().writeToFile('2')





