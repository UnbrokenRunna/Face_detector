from Detecting_movingobject import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool
import pandas as pd
from datetime import datetime


df['Start']= pd.to_datetime(df['Start'])
df['End']=pd.to_datetime(df['End'])
#df['Start']= df['Start'].apply(lambda x: pandas.to_datetime(x[0]))
#df['End']= df['End'].apply(lambda x: pandas.to_datetime(x[0]))
df['Start_string']=df['Start'].dt.strftime("%Y-%M-%D %H:%M:%S")
df['End_string']=df['End'].dt.strftime("%Y-%m-%d %H:%M:%S")


cds=ColumnDataSource(df)

p = figure(x_axis_type= 'datetime', height= 100, width = 500, title= 'Motion Graph')
p.yaxis.minor_tick_line_color=None
#p.yaxis.ticker=[0,1]
p.yaxis[0].ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[('Start','@Start_string',('End','@End_string'))])
p.add_tools(hover)

q = p.quad(left=df['Start'], right=df["End"], bottom = 0, top=1, color='green')

output_file('Graph1.html')

show(p)