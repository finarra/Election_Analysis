import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources', 'election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join('analysis','election_analyisis.txt')

#Open the elction results and read the file:
with open(file_to_load) as election_data:

#To do read and analyze data here.
    file_reader = csv.reader(election_data)

#print the header row.
    headers = next(file_reader)
    print(headers)

#print each row in the csv file
    for row in file_reader:
       print(row)



#using open function w mode

# with open(file_to_save, 'w') as txt_file:

#     txt_file.write('Counties in the Election\n')
#     txt_file.write('-------------------------\n')
#     txt_file.write('Araphoe\nDenver\nJefferson\n')






#Open the eleciton results and read the file


#To do: perform analusis

#Close the file.



#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.