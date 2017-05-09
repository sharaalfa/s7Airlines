import function

func = function.Calculator()
# create curve with w0 = w0opt and w1 = w1opt on scatter weight&height
w0opt, w1op1 = func.getMinOfLBFGS()
func.getChart(w0opt, w1op1)