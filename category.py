import index
import pandas
import function
# calculate the values of the future column of weight_category
function.Determinator().weight_category()
# read the resulting values
data = pandas.read_csv('temporary.csv')
# create new dataframe
data = pandas.DataFrame({'Weight': index.data['Weight'].values,
                         'Height': index.data['Height'].values,
                         'BMI': index.data['BMI'].values,
                         'Weight_category': data['Weight_category'].values})



