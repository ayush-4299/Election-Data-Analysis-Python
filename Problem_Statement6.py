#############################Problem 6: Election Trends Over Time (Visualization)#############################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df=pd.read_csv(r"C:\Users\ayush\OneDrive\Desktop\PythonCA2\Data.csv")

### Objective 1: Plot the number of elections held per year
elections_per_year = df.groupby("year")["ac_name"].nunique()
plt.figure(figsize=(10, 5))
sns.lineplot(x=elections_per_year.index, y=elections_per_year.values, marker="o", color="b")
plt.xlabel("Year")
plt.ylabel("Number of Elections")
plt.title("Number of Elections Held Per Year")
plt.grid(True)
plt.show()

###Objective 2: Create a line plot showing the voter turnout percentage trend over different years
df["turnout_percentage"] = pd.to_numeric(df["turnout_percentage"], errors='coerce')
turnout_trend = df.groupby("year")["turnout_percentage"].mean()
plt.figure(figsize=(10, 5))
sns.lineplot(x=turnout_trend.index, y=turnout_trend.values, marker="o", color="g")
plt.xlabel("Year")
plt.ylabel("Average Voter Turnout (%)")
plt.title("Voter Turnout Percentage Trend Over Years")
plt.grid(True)
plt.show()

###Objective 3: Visualize the number of candidates contesting each year using a bar chart
df["ac_total_candidates"] = pd.to_numeric(df["ac_total_candidates"], errors='coerce')
candidates_per_year = df.groupby("year")["ac_total_candidates"].sum()
plt.figure(figsize=(12, 6))
sns.barplot(x=candidates_per_year.index, y=candidates_per_year.values,palette="Blues_r")
plt.xlabel("Year")
plt.ylabel("Total Number of Candidates")
plt.title("Number of Candidates Contesting Each Year")
plt.xticks(rotation=45)
plt.show()
