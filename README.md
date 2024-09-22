# Python-challenge
Python-Challenge
Overview
This repository has two dedicated python folders - PyPoll and PyBank.
PyPoll
This task involves processing election data, stored in a csv file, to calculate the total votes cast, generate a list of candidates, track the number of votes each candidate received, and finally determine the winner. The results will be displayed in the console and saved to a         text file.
Files
election_data.csv: This file is in the Resources folder. It is the input file which contains poll data. The dataset is composed of three columns: "Voter ID", "County", and “Candidate”.
Analysis.txt: This file is in the Analysis folder. It is the output file where the results of the election will be saved.
main.py: The python script to execute and process the election data.

How the script works:
The script reads election data from the election_data.csv file in the Resources directory. Then it performs the following tasks:
    -Calculates the total number of votes.
    -Identifies all candidates.
    -Counts the votes each candidate received.
    -Calculates the percentage of total votes for each candidate.
    -Determines the winner based on the highest vote count.
Finally, the election results are printed to the console and saved to an Analysis.txt file in the Analysis directory.

How to Run
Ensure python 3 is installed before running the script. The election_data.csv file needs to be in a folder called 'Resources' which will be in the same directory as 'main.py'. Execute the Python script using the following command:  
python main.py  

Output:
The script will print the election results to the console.
It will also write the results to Analysis.txt in the Analysis/ folder.


PyBank
This task involves processing financial dataset, stored in a csv file, to calculate the total profit/loss over the entire period, the month-to-month changes in profit/loss, and identifying both the greatest increase and decrease in profits during the time frame. The results will      be displayed in the console and saved to a text file for easy reference. This task provides valuable insight into financial trends. 
Files
budget_data.csv: This file is in the Resources folder. It is the input file which contains profit/loss data. The dataset is composed of two columns: "Date", “Profit/Losses".
Budget_Analysis.txt: This file is in the Analysis folder. It is the output file where the results of the analysis will be saved.
main.py: The python script to execute and process the financial data.

How the script works:
    The script reads financial data from the budget_data.csv file in the Resources directory. Then it performs the following tasks:
    -the total number of months included in the dataset.
    -the net total amount of "Profit/Losses" over the entire period.
    -the changes in "Profit/Losses" over the entire period, and then the average of those changes.
    -the greatest increase in profits (date and amount) over the entire period.
    -the greatest decrease in profits (date and amount) over the entire period.
Finally, the results are printed to the console and saved to an Budget_Analysis.txt file in the Analysis directory.

How to Run
Ensure python 3 is installed before running the script. The budget_data.csv file needs to be in a folder called Resources which will be in the same directory as main.py. Execute the Python script using the following command:  python main.py  Output:
The script will print the results to the console.
It will also write the results to Budget-Analysis.txt in the Analysis folder.


Modifying the Script
If the structure of the CSV changes, the scripts needs to be modified accordingly.
