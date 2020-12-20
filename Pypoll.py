import os
import csv

# The data we need to retrieve
# Assign a variable for the file to load and path.
file_to_load=os.path.join("Resources","election_results.csv")

# Initialize total vote counter
total_votes= 0

#Candidates
candidate_options= []

#Candidate dictionary
candidate_votes= {}

# Winning Candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read file
with open (file_to_load) as election_data:
    
    # To do: read and analyze the data here
    file_reader= csv.reader(election_data)
    
    #Print each row in CSV file
    headers= next(file_reader)
    
    # To do:perform analysis
    for row in file_reader:
       
       # Add to total vote count
        total_votes += 1
        
        # print candidate name on each row
        candidate_name= row[2]
        
        #Add candidate name from each row
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
           
            #Begin tracking candidate's vote count
            candidate_votes[candidate_name]= 0

            # Add vote to candidates count
        candidate_votes[candidate_name] += 1
    
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        
        # retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        
        # Calaculate the percetage of votes
        vote_percentage = float(votes)/float(total_votes)*100
        
        # print out each candidate's name, vote count, and percentage of votes to terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # determine the winning vote count and candidate
        # determine if the votes are greater than the winning count
        if(votes>winning_count) and (vote_percentage>winning_percentage):
        
            # if this is true then winning_count=votes and winning percentage=vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # then winning_candidates=candidates name
            winning_candidate = candidate_name
        #print the candidate name and percentages 
    winning_candidate_summary = (f"-----------------\nWinner: {winning_candidate}\nWinning Vote Count: {winning_count:,}\nWinning Percentage: {winning_percentage: .1f}%\n-----------------")
print(winning_candidate_summary)
# Close the file
# 1. the total number of votes cast
# 2. A complete list of candidated who received votes
# 3. The percentage of voted each candidate won
# 4. The total number of votes each candidate wom
# 5. The winner of the election based on popular vote
# Create a filename variable to a direct or indirect path to the file.
file_to_save= os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write the data file
with open(file_to_save, "w") as txt_file:
# Write some data to file.
    txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")
