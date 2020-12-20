import os
import csv

# The data we need to retrieve
# Assign a variable for the file to load and path.
file_to_load=os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save= os.path.join("analysis", "election_analysis.txt")

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
    
    # Read header row
    headers= next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
       
        # Add to total vote count
        total_votes += 1
        
        # Get candidate name on each row
        candidate_name= row[2]
        
        # if the candidate doesn't match any existing candidate add to the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to candidate list
            candidate_options.append(candidate_name)
           
            #Begin tracking candidate's vote count
            candidate_votes[candidate_name]= 0

            # Add vote to candidates count
            candidate_votes[candidate_name] += 1
           
    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
    
        # print final vote count in terminal
        election_results = (f"\nElection Results\n-----------------\nTotal Votes: {total_votes:,}\n-----------------\n")
        print(election_results, end="")

        # Save the final vote count to the text file
        txt_file.write(election_results)

        # Iterate through the candidate list
        for candidate_name in candidate_votes:
                
            # retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]
                
            # Calaculate the percetage of votes
            vote_percentage = float(votes)/float(total_votes)*100
                
            # print out each candidate's name, vote count, and percentage of votes to terminal
            candidate_results= (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)

            # Save the candidates results to our text file
            txt_file.write(candidate_results)
                
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

        #print(winning_candidate_summary)
        print(winning_candidate_summary)

        txt_file.write(winning_candidate_summary)