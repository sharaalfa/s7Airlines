import data
import math
import pandas
import function2


# compute and save BMI
func = function2.Determinator()
func.createTemporaryFile('BMI')
for i in range(0, 25000):
    BMI = round(0.453*data.data['weight'].loc[i]/\
          math.sqrt(data.data['height'].loc[i]*0.025), 5)
    func.writeToFile(BMI)


# create common dataframe with BMI
data_BMI = pandas.read_csv('temporary.csv')
data = pandas.DataFrame({'BMI': data_BMI['BMI'].values,
                         'Height': data.data['height'].values,
                         'Weight': data.data['weight'].values})

# min and max BMI
function2.Determinator().maxAndMin(data['BMI'], 'BMI')

