import pandas as pd
import random
import csv
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()
mean = statistics.mean(data)
stddeviation = statistics.stdev(data)

print("Mean Of Pouplation = ",mean)
print("Standard Deveiation Of Pouplation = ",stddeviation)

def randomSet(counter):
    dataset = []
    for i in range(0,counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means= randomSet(100)
    mean_list.append(set_of_means)

std_deviation = statistics.stdev(mean_list)

firststdStart,firstStdEnd = mean - stddeviation,mean+stddeviation
secondstdStart,secondStdEnd = mean - (2*stddeviation),mean+(2*stddeviation)
thirdstdStart,thirdStdEnd = mean - (3*stddeviation),mean+(3*stddeviation)

df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()
meanOf3 = statistics.mean(data)
print("Mean Of SAMPLE 3 = ",meanOf3)

fig = ff.create_distplot([mean_list],["studentMarks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines", name = "MEAN"))
fig.add_trace(go.Scatter(x=[meanOf3,meanOf3],y=[0,0.17],mode="lines", name = "mean Of sample 3"))
fig.add_trace(go.Scatter(x=[secondStdEnd,secondStdEnd],y=[0,0.17],mode="lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[thirdStdEnd,thirdStdEnd],y=[0,0.17],mode="lines", name = "STANDARD DEVIATION 2"))
fig.show()

zScore = (mean-meanOf3)/stddeviation
print ("The Z Score Is = ", zScore)