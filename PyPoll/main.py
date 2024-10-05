# Import modules
import os
import csv
# File paths for input (election_data.csv) and output (Analysis.txt)
input_file = os.path.join('Resources', 'election_data.csv')
output_file = os.path.join('Analysis', 'Analysis.txt' )

# Initialize variables to store total votes, candidate names and total votes won by each candidate
total_votes = 0
candidate_list =[]
candidate_vote_count = []
candidate_one = 0
candidate_two = 0
candidate_three = 0

# Open and read the CSV file containing election data
with open(input_file, 'r') as election_file:
    csvreader = csv.reader(election_file)
    # skip the header row in csv file
    header = next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Increment the total vote count for each row
        total_votes += 1
        # The candidate's name is in the third column
        candidate = row[2] 

        # Add candidate to the candidate list if not already present
        if candidate not in candidate_list:
            candidate_list.append(candidate)

        # Count votes for each candidate based on their index in the 'candidate_list'    
        if candidate_list[0] == row[2]:
            candidate_one = candidate_one + 1
                       
        elif candidate_list[1] == row[2]:
            candidate_two = candidate_two + 1
               
        elif candidate_list[2] == row[2]:
            candidate_three = candidate_three + 1
            

   # Calculate percentage of votes for each candidate 
    candidate_one_percent = round(candidate_one/total_votes * 100, 3)
    candidate_vote_count.append(candidate_one)    #Add the total vote count for candidate one to the list
    candidate_two_percent = round(candidate_two/total_votes * 100, 3)
    candidate_vote_count.append(candidate_two)    #Add the total vote count for candidate two to the list
    candidate_three_percent = round(candidate_three/total_votes * 100, 3)
    candidate_vote_count.append(candidate_three)  #Add the total vote count for candidate three to the list

    # checking the winner of the election from the candidate vote count list
    max_vote = max(candidate_vote_count)
    # zip candidate_list and candidate_vote_count list to pair the values
    ziplist = zip(candidate_list, candidate_vote_count)

    #Loop through each row in the ziplist to find the winner of maximum votes
    winner = [row[0] for row in ziplist if row[1] == max_vote]
        

#Printing election results to terminal;
print("Election Results")
print('------------------------------------------')

print(f'Total Votes: {total_votes}')
print('---------------------------------------------')
print(f'{candidate_list[0]} : {candidate_one_percent}% ({candidate_one})')
print(f'{candidate_list[1]} : {candidate_two_percent}% ({candidate_two})')
print(f'{candidate_list[2]} : {candidate_three_percent}% ({candidate_three})')
print('----------------------------------------------')
print(f'Winner:  {winner}')
print('----------------------------------------------')

# Write the election results to the output file 
with open(output_file, 'w') as textfile:
    textfile.write("Election Results\n")
    textfile.write('----------------------------------------\n')
    textfile.write(f'Total Votes: {total_votes}\n')
    textfile.write('---------------------------------------------\n')
    textfile.write(f'{candidate_list[0]} : {candidate_one_percent}% ({candidate_one})\n')
    textfile.write(f'{candidate_list[1]} : {candidate_two_percent}% ({candidate_two})\n')
    textfile.write(f'{candidate_list[2]} : {candidate_three_percent}% ({candidate_three})\n')
    textfile.write('----------------------------------------------\n')
    textfile.write(f'Winner:  {winner}\n')
    textfile.write('----------------------------------------------\n')
