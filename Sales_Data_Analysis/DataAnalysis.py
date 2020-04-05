import pandas as pd
import os

df = pd.read_csv('./SalesData/Sales_April_2019.csv')
allMonthsData = pd.DataFrame()

file = [file for file in os.listdir('./SalesData')]

for f in file :
    df = pd.read_csv('./SalesData/' + f)
    allMonths = pd.concat([allMonthsData, df])

allMonthsData.to_csv("all_data.csv", index=False)
