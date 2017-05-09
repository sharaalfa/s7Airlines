import pandas
import function2

# read data and create dataframe
data = pandas.read_excel('weights_heights.csv')

data = pandas.DataFrame({"height":data['Height'].values,
                              "weight":data['Weight'].values})

# min and max height and weight
function2.Determinator().maxAndMin(data['height'], 'height')
function2.Determinator().maxAndMin(data['weight'], 'weight')
