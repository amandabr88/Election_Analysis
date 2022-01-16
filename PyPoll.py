# PyPoll.py
# 1. The data we need to retrieve
# 2. The total number of votes cast
# 3. A complete list of candidates who received votes
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}

# Create a county list and county votes dictionary.
counties = []
counties_votes={}

# Winning candidate and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest county and county voter turnout.
largest_county =""
largest_county_votes = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header
    header = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        
        # Print the candidate name from each row.
        candidate_name = row[2]

        # Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in counties:

             # Add the existing county to the list of counties.
             counties.append(county_name)

            # Begin tracking the county's vote count.
             counties_votes[county_name] = 0

        # Add a vote to that county's vote count.
        counties_votes[county_name] +=1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file: 
    
    #After opening the file print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    # Write a for loop to get the county from the county dictionary.
    for county in counties:
        # Retrieve the county vote count.
        county_votes = counties_votes.get(county)
        # Calculate the percentage of votes for the county.
        county_vote_percentage = float(county_votes) / float(total_votes) * 100

        # Print the county results to the terminal.
        county_results = (
            f"{county}: {county_vote_percentage:.1f}% ({county_votes:,})\n")
        print(county_results)
        
        # Save the county votes to a text file.
        txt_file.write(county_results)
        
        # Write an if statement to determine the winning county and get its vote count.
        if (county_votes > largest_county_votes):
            largest_county_votes = county_votes
            largest_county = county
            

    # Print the county with the largest turnout to the terminal.
    counties_summary = (
        f"-------------------------\n"
        f"Largest Country Turnout: {largest_county}\n"
        f"-------------------------\n")
    
    print(counties_summary)

    # Save the county with the largest turnout to a text file.
    txt_file.write(counties_summary)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes)/float(total_votes) * 100
        candidate_results =  (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"
            )
 
        # Print out each candidate's name, vote count, and percentage of votes to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            # if true set a winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate = candidate+name
            winning_candidate = candidate_name
    
    # Print out the winning candidate, vote count and percentage to terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    # Print the winning cancidate's results to the terminal
    print(winning_candidate_summary)
    # Save the winning cancidate's results to the txt file
    txt_file.write(winning_candidate_summary)


