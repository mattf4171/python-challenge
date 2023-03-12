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
df = pd.read_csv('/Users/matthewfernandez/Desktop/UCB/Module3Challenge/PyBank/Resources/budget_data.csv')

print("Financial Analysis\n----------------------------")

# Calculate all desired variables to print 
totalMonths = df['Date'].size
total = df['Profit/Losses'].values.sum()
avgChange = df['Profit/Losses'].values.mean()
greatIncProfit = df['Profit/Losses'].values.max()
greatDecProfit = df['Profit/Losses'].values.min()

# print variables like the provided format
print("Total Months: {}".format(totalMonths))
print("Total: ${}".format(total))
print("Average Change: ${:.2f}".format(avgChange))
print("Greatest Increase in Profits: ${}".format(greatIncProfit))
print("Greatest Decrease in Profits: ${}".format(greatDecProfit))


# write to .txt file same format as in terminal cosole
with open('analysis/output.txt','a') as f:
    f.write("Total Months: {}".format(totalMonths))
    f.write("Total: ${}".format(total))
    f.write("Average Change: ${:.2f}".format(avgChange))
    f.write("Greatest Increase in Profits: ${}".format(greatIncProfit))
    f.write("Greatest Decrease in Profits: ${}".format(greatDecProfit))

