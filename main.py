from pandas import *

data = pandas.read_csv('ratings.csv')
data.head(3)
print('32131')
data['rating'].min()
data['rating'].max()

rating_count = data.groupby('userId').count().reset_index()['userId', 'moveId']
rating_count.head()

fans_data = data[data['userId'].isin(fans)]
print(fans_data.head(2))

min_max = fans_data.groupby('userId').agg({'timestamp':['min', 'max']})
min_max.head(3)
min_max['timelife'] = min_max['timestamp']['max'] - min_max['timestamp']['min']
min_max['timelife'] = min_max['timelife'] / (24 * 3600)
min_max['timelife'] = min_max.apply(lambda x : int(x['timelife']), axis=1)
print(min_max['timelife'].mean)

data[data['userId']== 1]['rating'].value_counts()



