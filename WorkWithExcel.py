import pandas as pd

fileName1 = 'PRCp_1.xlsx'
fileName2 = 'PRCp_2.xlsx'

df1 = pd.read_excel(fileName1)
#df2 = pd.read_excel(fileName2)

#split_values1 = df1['Name'].unique()
#split_values2 = df2['Name'].unique()

# will create a new excel file for each unique name
#for value in split_values1:
 #   fromDf1 = df1[df1['Name'] == value]
  #  output_file_name = str(value) + ".xlsx"
   # fromDf1.to_excel(output_file_name)

#print(df)
#print(split_values1)
#print(split_values2)


