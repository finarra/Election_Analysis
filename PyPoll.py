import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources', 'election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join('analysis','election_analyisis.txt')
#Add accumulator of total votes:
total_votes = 0
#create candidate_options list:
candidate_options = []
#declare empty candidate dictionary to add candidate name and his votes {'candidate1':votes, etc}:
candidate_votes = {}
#Winning candidate and winning count tracker
winning_candidate = ' '
winning_count = 0
winning_percentage = 0

#Open the elction results and read the file:
with open(file_to_load) as election_data:

#To do read and analyze data here.
    file_reader = csv.reader(election_data)

#skip the header row and print the headers.
    headers = next(file_reader)
   # print(headers)

#print each row in the csv file
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1    
        #print the candidate name from each row.
        candidate_name = row[2]
        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #add it to the list of canddiate
            candidate_options.append(candidate_name)
            #track each candidate's vote count starting from zero:
            candidate_votes[candidate_name] =0
        candidate_votes[candidate_name] += 1

#Determine the percentage of votes for each candidate by looping through the counts:
#1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    #2. retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    #3. calculate the percentage of votes, convert to float to get decimal numbers:
    vote_percentage = float(votes) / float(total_votes)*100.
    #4. Print the candidate name and percentage of votes.
    #print(f'{candidate_name}: received {vote_percentage: .1f}% of the vote.')
    #Determine winning vote count and candidate:
    #1. Determine if the votes are greater than the winning count.
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        #2. If true then set winning_count = votes and winning_percent = vote percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        #3. set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name
   
   #todo: print out each candidate's name, vote count and percentage of votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
#winning candidate summary
winning_candidate_summary = (
    f"----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count: ,}\n"
    f"Winning Percentage: {winning_percentage: .1f}%\n"
    f"----------------------\n")
print(winning_candidate_summary)