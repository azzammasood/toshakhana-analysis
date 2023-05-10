## List of possible questions
# What is the total value of all gifts received by former government officials from foreign leaders and dignitaries?
# Which specific individuals received gifts from the Toshakhana, and what were those gifts?
# Did any government officials declare the gifts they received to the Pakistani government or pay taxes on them?
# Were there any patterns or trends in the types of gifts received by different officials or from different countries?

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.express as px
import pandas as pd 
import matplotlib.pyplot as plt

tosha = pd.read_csv('datasets/Refined_TK_data ver 2.csv')

# Data Cleaning
tosha = tosha[tosha['Assessed Value'].notna()]

# Answering the first question
print('Total value of all gifts:', sum(tosha['Assessed Value']))

# Answering the second question
# Group the dataset by recipient and calculate the total assessed value and retention cost for each recipient
recipient_df = tosha.groupby('Name of Recipient').agg({'Assessed Value': 'sum', 'Retention Cost': 'sum'}).reset_index()
# Create an interactive scatter plot using Plotly Express
fig = px.scatter(recipient_df, x='Assessed Value', y='Retention Cost', color='Name of Recipient', size='Assessed Value', hover_name='Name of Recipient')
# Customize the plot layout
fig.update_layout(title='Total Assessed Value and Retention Cost by Recipient',
                  xaxis_title='Total Assessed Value of Gifts (PKR)',
                  yaxis_title='Total Retention Cost (PKR)',
                  font=dict(family='sans-serif', size=12, color='#333333'))
# Show the plot
fig.show()

# Answering the third question
tosha_q3 = tosha[tosha['Retained'] != 'Yes']
tosha_q3 = tosha_q3[tosha_q3['Retention Cost'] > 0]
print(len(tosha_q3))

# Answering the fourth question
dup = tosha[tosha['Item Category'].duplicated() == True]
print(dup['Item Category'].value_counts())
print("The trend is that {0} are gifted the most with a count of {1}".format(dup['Item Category'].value_counts().index[0], dup['Item Category'].value_counts()[0]))
# Visualization through bar graph
x = dup['Item Category'].value_counts()
x = x[x > 11].index
y = dup['Item Category'].value_counts()
y = y[y > 11]
plt.bar(x, y)
