#import modules
import os
import csv

#Variable, List, and Dictionary definition
monthcount = 1
pl_total = 0
bankar = dict()
change_total = 0
this_month = []
last_month = []
difference = []
zip_difference = zip()


#finding location of data
location = "C:\\Users\\ZPurinton\\Documents\\Personal\\Data Boot Camp\\Homework\\python-challenge\\PyBank\\Resources"
bankfile = os.path.join(location, "Unit 3 - Python_HomeWork_Instructions_PyBank_Resources_budget_data.csv")

print(bankfile)

#Reading csv file
with open(bankfile, "r") as file:
    bank = csv.reader(file, delimiter = ",")

#For loop to load data into dictionay and lists
    for row in bank:
        if monthcount == 1:
            monthcount += 1
        else:
            monthcount += 1
            priormonth = monthcount - 1
            pl_total = pl_total + int(row[1])
            bankar[monthcount] = {"date":row[0],
                      "pl":row[1]}
 
#Creating lists to calculate difference in Profits/Losses from month to month
            if priormonth > 2:
                this_month.append(bankar[monthcount]['pl'])
                last_month.append(bankar[priormonth]['pl'])
                
#Converting Profits/Losses to integers    
    this_month = [int(i) for i in this_month]
    last_month = [int(i) for i in last_month]

            
    zip_difference = zip(this_month, last_month)
    print(zip_difference)
    for this_month, last_month in zip_difference:
        difference.append(this_month - last_month)
    difference = [int(i) for i in difference]
    
#Defining Max and Min change in Profit/Loss
    greatInc = max(difference)
    greatDec = min(difference)
    
#Average change in Profit/Loss
    ave_change = (sum(difference))/(monthcount-2)

   

#Printing Output  
    print(f"Total Months: {monthcount - 2}")
    print(f"Total: {pl_total}")
    print(f"Average Change: {ave_change}")
    print(f"Greatest Increase in Profits: {greatInc}")
    print(f"Greatest Decrease in Progits: {greatDec}")

#Output to text file
locationA = "C:\\Users\\ZPurinton\\Documents\\Personal\\Data Boot Camp\\Homework\\python-challenge\\PyBank\\analysis"
bankoutput = os.path.join(locationA, "bankoutput.txt")
with open("bankoutput.txt", "w") as f:
    print(f"Total Months: {monthcount - 2}")
    print(f"Total: {pl_total}")
    print(f"Average Change: {ave_change}")
    print(f"Greatest Increase in Profits: {greatInc}")
    print(f"Greatest Decrease in Progits: {greatDec}")
    

        
    