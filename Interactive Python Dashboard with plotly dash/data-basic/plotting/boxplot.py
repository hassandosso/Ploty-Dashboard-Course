import plotly.offline as pyo
import plotly.graph_objs as go

#y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

data = [go.Box(y=snodgrass,name='snodgrass'),
        go.Box(y=twain,name='twain')]

# to see only outliers, boxpoints='outliers'
pyo.plot(data)