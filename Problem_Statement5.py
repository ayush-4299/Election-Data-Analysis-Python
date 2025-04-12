#############################Problem 5: Party Dominance Over Elections#############################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df=pd.read_csv(r"C:\Users\ayush\OneDrive\Desktop\PythonCA2\Data.csv")

###Objective 1: Find out which party won the most elections across all years
# Count number of times each party won (position = 1)
party_wins = df[df["position"] == 1]["party"].value_counts()
print("Party with the most election wins:")
print(party_wins)

###Objective 2: Identify parties that consistently finish in the top 3 positions
# Count occurrences of each party finishing in top 3 positions
top_3_parties = df[df["position"] <= 3]["party"].value_counts()
print("Parties that consistently finish in the top 3 positions:")
print(top_3_parties)

###Objective 3: Calculate the average vote share of the top 5 parties
# Get the top 5 parties by total wins
top_5_parties = party_wins.index[:5]
# Calculate the average vote share for each of the top 5 parties
avg_vote_share_top_5 = df[df["party"].isin(top_5_parties)].groupby("party")["vote_share_percentage"].mean()
print("Average Vote Share of the Top 5 Parties:")
print(avg_vote_share_top_5)

###Objective 4: Determine if any party has won with a vote share greater than 70%
high_margin_wins = df[(df["position"] == 1) & (df["vote_share_percentage"] > 70)]
print("Instances where a party won with vote share > 70%:")
print(high_margin_wins[["year", "state_name", "ac_name", "party", "vote_share_percentage"]])

