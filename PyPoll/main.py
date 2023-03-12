"""
Matthew Fernandez
3/11/23

Description:
Script using pandas to extract data most efficiently
"""

import os 
import sys
import pandas as pd 

# read in csv file as dataframe df
df = pd.read_csv('/Users/matthewfernandez/Desktop/UCB/Module3Challenge/PyPoll/Resources/election_data.csv')

# sum up all unique
totalVotes = df['Ballot ID'].size
normalizedCandidates = (df['Candidate'].value_counts(normalize=True).sort_index().values) * 100
countOfCandidates = df['Candidate'].value_counts().sort_index().values
sortedNames = df['Candidate'].value_counts().sort_index().index

# print all desired variables 
print("Election Results\n-------------------------\nTotal Votes: {}\n-------------------------".format(totalVotes))
for _,i in enumerate(sortedNames):
    print("{}: {:.3f}% ({})".format(i,normalizedCandidates[_], countOfCandidates[_]))

print("-------------------------")
print("Winner: {}\n-------------------------".format(df['Candidate'].value_counts().sort_values(ascending=False).index[0]))

# method to write exact output to output.txt file in analysis directory
with open('analysis/output.txt','a') as f:
    f.write("Election Results\n-------------------------\nTotal Votes: {}\n-------------------------".format(totalVotes))
    for _,i in enumerate(sortedNames):
        f.write("\n{}: {:.3f}% ({})".format(i,normalizedCandidates[_], countOfCandidates[_]))

    f.write("\n-------------------------")
    f.write("\nWinner: {}\n-------------------------".format(df['Candidate'].value_counts().sort_values(ascending=False).index[0]))

