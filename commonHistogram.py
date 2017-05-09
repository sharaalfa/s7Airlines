import data
import function

func = function.Determinator()
func.createHist(data.data['height'], 211, 15, 'height', 0.25)
func.createHist(data.data['weight'], 212, 100, 'weight', 0.05)

