from pathlib import Path
import csv

#set path for csv
csvpath = Path('Resources/budget_data.csv')

#set variables
totalMonths = 0
netProfit = 0
totalProfit = 0
startProfit = 0
profitChange = 0
maxProfit = 0
minProfit = 9999
maxDate = ""
minDate = ""
netProfitList = []

#csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    #skip header row
    csvheader = next(csvreader)
    firstRow = next(csvreader)    
    previousProfit = int(firstRow[1])
    totalMonths = 1
    totalProfit = int(firstRow[1])

    #read each row of data after header 
    for row in csvreader:
        date = row[0]
        profit = int(row[1])
        totalProfit += profit

        totalMonths += 1
        netProfit = profit - previousProfit
        netProfitList += [netProfit]
        previousProfit = profit
        if netProfit > maxProfit:
            maxProfit = netProfit
            maxDate = date

        if netProfit < minProfit:
            minProfit = netProfit
            minDate = date

    averageProfit = sum(netProfitList) / len(netProfitList)

    print("Financial Analysis")       
    print("-------------------")
    print(f"Total Number of Months: {totalMonths}")
    print(f"Total Profit: ${totalProfit}")
    print(f"Average Profit Change: ${averageProfit:.2f}")
    print(f"Greatest Increase in Profits: {maxDate}, ${maxProfit}")
    print(f"Greatest Decrease in Profits: {minDate}, ${minProfit}")
