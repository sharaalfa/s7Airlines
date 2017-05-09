import index
import function


x = index.data['Weight'].values
y = index.data['Height'].values
z = index.data['BMI'].values

# get picture pair ralations x, y and z
function.Determinator().createPair(x, y, z)


# box
#index.data.plot(kind='box')

# scatter
#index.data[['BMI', 'Height']].plot(x='BMI', y='Height', kind='scatter')
#index.data[['BMI', 'Weight']].plot(x='BMI', y='Weight', kind='scatter')
#index.data[['Height', 'Weight']].plot(x='Height', y='Weight', kind='scatter')
#plt.show()