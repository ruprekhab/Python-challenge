# Import modules
import os
import csv

# File paths for input (budget_data.csv) and output (Budget_Analysis.txt)
file_path = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join("Analysis", "Budget_Analysis.txt")

# Initialize variables to store total months, list of monthly profit/loss changes, and dates
total_months = 1
change_list = []
dates = []


# Open and read the CSV file containing budget data
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip the header row in csv file
    header_row = next(csvreader)
    
    # Extract and store the first row of data
    first_row = next(csvreader)

    # Initialize variables for calculating total profit/loss and the last month's profit/loss for change calculation
    last_profit_loss = int(first_row[1])
    total_profit_loss = last_profit_loss
       
    # Loop through each row in the CSV file to process monthly data
    for row in csvreader:  
        
        date = row[0]
        total_months = total_months + 1  #Increment the total months count            

        # Extract the current month's profit/loss and add to the total net profit/loss
        current_profit_loss = int(row[1])
        total_profit_loss =  total_profit_loss + current_profit_loss
        # Calculate the monthly change in profit/loss compared to the last month
        change = current_profit_loss - last_profit_loss
        change_list.append(change)      #Add the monthly change to the list
        dates.append(date)              #Add current date to the list
        last_profit_loss = current_profit_loss  #Update the last month's profit/loss to calculate the next change

      
    
    # calculate the average change in profit/loss over the entire period
    average_change = round(sum(change_list)/len(change_list),2)

    # set variables for the greatest increase and decrease in profits/loss over the entire period
    max_increase = max(change_list)  
    max_decrease = min(change_list) 

    # Zip 'change_list' and 'dates' lists
    summary_change = list(zip(change_list, dates)) 

    # Loop through Summary_change to find the greatest increase and decrease in profit/Loss
    date_max = [row[1] for row in summary_change if row[0]==max_increase]
    date_min = [row[1] for row in summary_change if row[0] == max_decrease]

            

    #Print the results to the terminal
    print("Financial Analysis")
    print('----------------------------------------')
    
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}")   
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {date_max} (${max_increase})")
    print(f"Greatest Decrease in Profits: {date_min} (${max_decrease})")
   
   
# Export results to a text file 
with open(output_path, 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write('----------------------------------------\n')   
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total_profit_loss}\n")
    textfile.write(f"Average Change: ${average_change}\n")
    textfile.write(f"Greatest Increase in Profits: {date_max} (${max_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {date_min} (${max_decrease})\n")


    

    
        

 
            
            
                                
    

    
    








