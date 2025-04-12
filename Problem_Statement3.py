#############################Problem 3:Election Competitiveness Analysis#############################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df=pd.read_csv(r"C:\Users\ayush\OneDrive\Desktop\PythonCA2\Data.csv")

###Objective 1: Find the percentage of elections where the winning margin was below 5%
# Convert margin percentage to numeric
df['margin_percentage'] = pd.to_numeric(df['margin_percentage'], errors='coerce')

# Calculate percentage of elections where margin was below 5%
close_elections = df[df['margin_percentage'] < 5].shape[0]
total_elections = df.shape[0]
close_elections_percentage = (close_elections / total_elections) * 100

print(f"Percentage of elections with a winning margin below 5%: {close_elections_percentage:.2f}%")

###Objective 2: Identify constituencies with the closest competition (smallest margin percentage)
# Find the constituency with the smallest margin percentage
closest_competition = df[df['margin_percentage'] == df['margin_percentage'].min()]
print("Constituency with the closest competition:")
print(closest_competition[['ac_name', 'state_name', 'year', 'margin_percentage']])

###Objective 3: Compute the average number of candidates contesting in a constituency per election
# Compute average number of candidates per constituency per election
avg_candidates_per_constituency = df.groupby(['year', 'ac_name'])['ac_total_candidates'].mean().mean()
print(f"Average number of candidates per constituency per election: {avg_candidates_per_constituency:.2f}")

###Objective 4: Analyze the effect of multi-candidate races on vote share distribution(Visualization)
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['ac_total_candidates'], y=df['vote_share_percentage'], alpha=0.5)
plt.xlabel("Number of Candidates")
plt.ylabel("Vote Share Percentage")
plt.title("Effect of Multi-Candidate Races on Vote Share")
plt.show()
