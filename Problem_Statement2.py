#############################Problem 2:Constituency-Level Election Insights##############################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df=pd.read_csv(r"C:\Users\ayush\OneDrive\Desktop\PythonCA2\Data.csv")

###Objective 1: Identify constituencies with the highest and lowest number of candidates
# Count candidates per constituency
candidates_per_constituency = df.groupby('ac_name')['candidate_name'].nunique()
# Find the highest and lowest
highest_constituency = candidates_per_constituency.idxmax()
lowest_constituency = candidates_per_constituency.idxmin()
print(f"Constituency with highest candidates:{highest_constituency}({candidates_per_constituency.max()} candidates)")
print(f"Constituency with lowest candidates:{lowest_constituency}({candidates_per_constituency.min()} candidates)")

###Objective 2: Find the constituency where the winning margin was the highest
# Find constituency with the highest winning margin
highest_margin = df.loc[df['margin'].idxmax()]
print(f"Constituency with highest winning margin: {highest_margin['ac_name']} ({highest_margin['margin']} votes)")

###Objective 3: Determine the average vote share of winning candidates in each constituency
# Get only winners (position == 1) and calculate average vote share per constituency
avg_vote_share_per_constituency = df[df['position'] == 1].groupby('ac_name')['vote_share_percentage'].mean()
# Display first few results
print(avg_vote_share_per_constituency.head())

###Objective 4: Compare the number of male and female candidates contesting per constituency
# Count number of male and female candidates per constituency
gender_distribution = df.groupby(['ac_name', 'sex'])['candidate_name'].count().unstack()
# Display results
print(gender_distribution.head())

