#! /usr/bin/python
# -*- encoding: UTF-8 -*-
import category
import seaborn as sns


# show boxplot weight_category from height
sns.boxplot(x=category.data['Weight_category'].values, y=category.data['Height'].values)
sns.utils.axlabel(u'Весовая категория', u'Рост')
sns.plt.show()