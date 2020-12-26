import os
import csv

#open input file
input_data_csv = os.path.join( "Resources", "election_data.csv")

#open output file
output_file = os.path.join("Analysis","Eletion_analysis.txt")

# dictionary of candidates and total votes per candidate
votes_per_candidate = {}
# List of all votes 
votes=[]
# lis of candidates (Unique)
unique_candidates=[]
# Grand Total of votes
total_votes = 0

with open(input_data_csv) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip the header
    csv_header = next(csvfile)

    for row in csvreader:
        # store values in votes list
        votes.append(row[2])
 
    def unique(list1): 
        # traverse for all elements 
        for x in list1: 
            # check if exists in unique_list or not. If not store the candidate name
            if x not in unique_candidates: 
                unique_candidates.append(x)  
    
    # Function to calculate votes per candidate
    def countVotes(candidatelist, votelist):
        
        # initialize the total votes per candidate with zero for each candidate
        for x in candidatelist:
            votes_per_candidate[x] = 0
        # For eqach candidate in the dictionary add the votes from the votes list
        for y in votelist:
            votes_per_candidate[y] += 1
    
    # Call funciton unique with the parameter vote list
    unique(votes)
    # Call funciton countvotes() with paramter unique list of candidates and votes list
    countVotes(unique_candidates, votes)
    max_vote = max(votes_per_candidate.values())
    total_votes= sum(votes_per_candidate.values())
    max_candidate = [k for k, v in votes_per_candidate.items() if v == max_vote]
    
    #Print results to the terminal
    print("Election Results")
    print("---------------------")
    print(f"total votes {total_votes}")
    print("----------------------")
    for l in unique_candidates:
        print(f" {l} {round(((votes_per_candidate[l]/total_votes)*100),2)} %    ({votes_per_candidate[l]}) ") 
    print("-----------------------")
    print(f"Winner: {max_candidate[0]}")
    
    #write to output into q text file
    output_file1 = open(output_file,"w")
    output_file1.write('Election Results\n')
    output_file1.write('----------------------------\n')
    output_file1.write('Total Votes    ') 
    output_file1.write(str(total_votes))
    output_file1.write('\n')
    output_file1.write('----------------------------\n')
    for m in unique_candidates:
        output_file1.write(m)
        output_file1.write('  ')
        output_file1.write(str(round(((votes_per_candidate[m]/total_votes)*100),2)))
        output_file1.write('%')
        output_file1.write('  ')
        output_file1.write(str(votes_per_candidate[m]))
        output_file1.write('\n')
    output_file1.write('-----------------------------\n')
    output_file1.write('Winner ')
    output_file1.write(max_candidate[0])
