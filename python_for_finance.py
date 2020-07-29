import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#start = dt.datetime(2000,1,1)
#end = dt.datetime.now()

#df = web.DataReader('RLOG3.SA','yahoo', start, end)
#df.to_csv('RLOG.csv')

#Function used to read csv files
#Using the option to parse dates
#Selecting the first column as the index
df = pd.read_csv('RLOG.csv', parse_dates = True, index_col = 0)

#Used to plot a graph with the selected column and to shw to us
df['Adj Close'].plot()
plt.show()
#print(df.head())
