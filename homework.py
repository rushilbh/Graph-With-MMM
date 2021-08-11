#import pandas,csv,plotly.express
import csv 
import pandas as pd
import plotly.express as px

#opening csv file and reading it
with open( 'class2.csv', newline='') as fd:
    reader = csv.reader(fd)
    file_data = list(reader)

# To remove the headers of our data
file_data.pop(0)

total_marks = 0
total_entries = len(file_data)

#loop for adding marks 
for m in file_data:
    total_marks += float(m[1])

#finding mean
mean = total_marks / total_entries
print("Mean(Average) :-" + str(mean))

#ploting graphs

fd = pd.read_csv('class2.csv')
fig = px.scatter(fd, x = 'Student Number', y = 'Marks')
fig.update_layout(shapes=[
dict(
    type='line',
    y0=mean,y1=mean,x0=0,x1=total_entries

)
])
fig.show()



