##############################Problem 1: Election Results Trends##############################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df=pd.read_csv(r"C:\Users\ayush\OneDrive\Desktop\PythonCA2\Data.csv")

###Objective 1: Find the number of unique elections (years and states) in the dataset
# Count unique elections (year, state_name)
unique_elections = df[['year', 'state_name']].drop_duplicates().shape[0]
print("Total Unique Elections:", unique_elections)

###Objective 2: Identify the state that has had the most election events
# Count number of elections per state
state_election_counts = df.groupby('state_name')['year'].nunique()
# Find state with the most elections
most_elections_state = state_election_counts.idxmax()
most_elections_count = state_election_counts.max()
print(f"State with most elections: {most_elections_state} ({most_elections_count} elections)")

###Objective 3: Determine how many unique candidates participated across all elections
# Count unique candidates
unique_candidates = df['candidate_name'].nunique()
print("Total Unique Candidates:", unique_candidates)

###Objective 4: Find the total number of constituencies contested in all elections
# Count unique constituencies
unique_constituencies = df['ac_name'].nunique()
print("Total Unique Constituencies:", unique_constituencies)

