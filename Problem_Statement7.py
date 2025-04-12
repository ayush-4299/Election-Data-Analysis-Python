##########################Problem 7:Vote Share Distribution Across Parties(Visualization)#############################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df=pd.read_csv(r"C:\Users\ayush\OneDrive\Desktop\PythonCA2\Data.csv")

#Using Seaborn
###Objective 1: Generate a histogram of vote share percentages to see the spread of votes
plt.figure(figsize=(10, 6))
sns.histplot(df["vote_share_percentage"], bins=20, kde=True, color="blue")
plt.xlabel("Vote Share Percentage")
plt.ylabel("Frequency")
plt.title("Distribution of Vote Share Percentages")
plt.show()

###Objective 2: Plot a pie chart showing the percentage of total votes received by the top 5 parties
party_votes = df.groupby("party")["total_votes"].sum()
top_5_parties = party_votes.nlargest(5)
plt.figure(figsize=(8, 8))
plt.pie(top_5_parties,labels=top_5_parties.index,autopct="%1.1f%%",startangle=140,colors=["blue","red","green",
                                                                                          "orange","purple"])
plt.title("Total Votes Received by Top 5 Parties")
plt.show()

###Objective 3: Display a bar chart comparing the average vote share of male vs. female candidates
df["sex"] = df["sex"].str.strip().str.upper()
gender_vote_share = df.groupby("sex")["vote_share_percentage"].mean()
plt.figure(figsize=(8, 6))
sns.barplot(x=gender_vote_share.index, y=gender_vote_share.values, palette="coolwarm")
plt.xlabel("Gender")
plt.ylabel("Average Vote Share (%)")
plt.title("Average Vote Share of Male vs. Female Candidates")
plt.show()




