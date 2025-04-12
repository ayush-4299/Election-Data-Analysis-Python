##########################Problem 4: Candidate Performance Based on Age##############################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df=pd.read_csv(r"C:\Users\ayush\OneDrive\Desktop\PythonCA2\Data.csv")

###Objective 1: Determine the average age of winning candidates per state
# Convert age to numeric
df['age'] = pd.to_numeric(df['age'], errors='coerce')
# Get only winning candidates (position = 1) and calculate the average age per state
winning_candidates = df[df['position'] == 1]
avg_winner_age_per_state = winning_candidates.groupby("state_name")["age"].mean()
print(avg_winner_age_per_state)

###Objective 2: Identify the youngest and oldest candidates who have won an election
youngest_winner = winning_candidates.loc[winning_candidates['age'].idxmin()]
oldest_winner = winning_candidates.loc[winning_candidates['age'].idxmax()]
print("Youngest Winning Candidate:", youngest_winner[['candidate_name', 'age', 'state_name', 'year']])
print("Oldest Winning Candidate:", oldest_winner[['candidate_name', 'age', 'state_name', 'year']])

###Objective 3: Find out if younger candidates have a higher or lower success rate
# Define a threshold for younger candidates (e.g., below median age)
median_age = df['age'].median()
young_candidates = df[df['age'] < median_age]
old_candidates = df[df['age'] >= median_age]
young_success_rate = (young_candidates[young_candidates['position'] == 1].shape[0]/young_candidates.shape[0])*100
old_success_rate = (old_candidates[old_candidates['position'] == 1].shape[0]/old_candidates.shape[0])*100
print(f"Success Rate of Younger Candidates: {young_success_rate:.2f}%")
print(f"Success Rate of Older Candidates: {old_success_rate:.2f}%")

###Objective 4: Analyze the distribution of ages among all candidates (Visualization)
plt.figure(figsize=(10, 6))
sns.histplot(df['age'], bins=20, kde=True, color="blue")
plt.xlabel("Candidate Age")
plt.ylabel("Frequency")
plt.title("Distribution of Candidate Ages")
plt.show()

