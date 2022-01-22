# Import Dependencies.
import csv
import os

#File import and writing

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")


#Initializing Variables

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#County Data

#list to hold county names
county_options = []
#dictionary to hold votes 
county_votes = {}
#county name with highest turnout
turnout_county = ""
#amount of votes cast in highest turnout county
turnout_total = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        #get county name
        county_name = row[1]

        if candidate_name not in candidate_options:

           # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        #Check and count votes per county
        if county_name not in county_options:

            # Add new county
            county_options.append(county_name)

            # Begin count
            county_votes[county_name] = 0

        # Add vote to the county
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    ###
    # FINAL VOTE COUNT
    ###

    # Final results, initiallize county formatting
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n")
    print(election_results, end="")
    
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    ###
    # County Analysis
    ###

    #Header for county analysis
    county_header = (
        f"County Results:\n")

    print(county_header, end="")
    txt_file.write(county_header)

    # Loop by county
    for county_name in county_votes:
        # Retrieve total votes from county
        votes = county_votes[county_name]
        # Calculate percent of county per total votes
        turnout_percentage = float(votes) / float(total_votes) * 100

        county_results = (f"{county_name}: {turnout_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(county_results)
        #  Save the candidate results to our text file.
        txt_file.write(county_results)

        # Determine county with the highest turnout
        if (votes > turnout_total):
            turnout_county = county_name
            turnout_total = votes

    turnout_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {turnout_county}\n"
        f"-------------------------\n")

    #Write turnout results to module and txt file
    print(turnout_summary)
    txt_file.write(turnout_summary)

    ###
    # Winner Analysis
    ###


    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.

    txt_file.write(winning_candidate_summary)
        