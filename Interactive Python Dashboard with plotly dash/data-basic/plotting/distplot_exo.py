import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv('Data/iris.data',sep=',',names=['sepal length','sepal width','petal length','petal width','class'])
#print(df.head())
#print(df.columns)
iris_setosa = df[df['class']=='Iris-setosa']['petal length']
iris_versicolor = df[df['class']=='Iris-versicolor']['petal length']
iris_virginica = df[df['class']=='Iris-virginica']['petal length']

hist_data =[iris_setosa,iris_virginica,iris_versicolor,]
group_labels =['iris setosa','iris virginica','iris versicolor']

fig = ff.create_distplot(hist_data,group_labels,bin_size=[0.1,0.2,0.3])
pyo.plot(fig)
