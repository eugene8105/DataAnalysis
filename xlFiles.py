import xlrd

path = "PartReport.xlsx"

inputWorkbook = xlrd.open_workbook(path)
inputWorksheet = inputWorkbook.sheet_by_index(0)


    #.nrows and .ncols will print how many rows and columns
'''
print(inputWorksheet.nrows)
print(inputWorksheet.ncols)

print(inputWorksheet.cell_value(1,0))
print(inputWorksheet.cell_value(1,11))
'''
partName = []
cycleTime = []

for i in range(1,inputWorksheet.nrows) :
    partName.append(inputWorksheet.cell_value(i,0))
    cycleTime.append(inputWorksheet.cell_value(i,11))

print(partName)
'''
    'w' meens - write.
    'r' meens - read.
    will open the file and erace all data
'''
testText = 'some ,test text \nNew line test'
saveToFile = open('testFile.csv','w')
saveToFile.write(testText)
saveToFile.close()