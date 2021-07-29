import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
# Reading scores data
df = pd.read_csv(r'F:\Python Projects\Normal Distribution\StudentsPerformance.csv')
data = df["reading score"].to_list()

# calculating the mean, median, mode and the standard deviation
mean = sum(data)/len(data)
median = st.median(data)
mode = st.mode(data)
std_dev = st.stdev(data)

# Finding first, second and third standard deviation start and end velues
first_stdev_start,first_stdev_end = mean-std_dev,mean+std_dev
second_stdev_start,second_stdev_end = mean-(2*std_dev),mean+(2*std_dev)
third_stdev_start,third_stdev_end = mean-(3*std_dev),mean+(3*std_dev)

# Ploting chart
fig = ff.create_distplot([data],["reading score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode = "lines",name="mean"))

fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.17],mode='lines',name='standard_deviation_one_start'))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode='lines',name='standard_deviation_one_end'))

fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.17],mode='lines',name='standard_deviation_second_start'))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode='lines',name='standard_deviation_second_end'))

fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.17],mode='lines',name='standard_deviation_third_start'))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode='lines',name='standard_deviation_third_end'))
fig.show()

list_of_data_within_1_standard_deviation = [result for result in data if result>first_stdev_start and result<first_stdev_end]
list_of_data_within_2_standard_deviation = [result for result in data if result>second_stdev_start and result<second_stdev_end]
list_of_data_within_3_standard_deviation = [result for result in data if result>third_stdev_start and result<third_stdev_end]

print('Mean {}'.format(mean))
print('Median {}'.format(median))
print('Mode {}'.format(mode))
print('Standard Deviation {}'.format(std_dev))

print('{}% of data lies within 1 standard deviation'.format(len(list_of_data_within_1_standard_deviation)*100.0/len(data)))
print('{}% of data lies within 2 standard deviation'.format(len(list_of_data_within_2_standard_deviation)*100.0/len(data)))
print('{}% of data lies within 3 standard deviation'.format(len(list_of_data_within_3_standard_deviation)*100.0/len(data)))