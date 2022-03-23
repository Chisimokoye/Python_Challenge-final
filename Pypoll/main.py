import os 
import csv 

csv_path = os.path.join("..","..", "Python-Challenge", "Pypoll", "resources", "election_data.csv")

candidates = []
Ballot_Id = []
county = []
Charles = []
Diana = []
Raymon = []


with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
   # print (csvreader)
    #read header row first
    csv_header = next(csvreader)
   # print(f'CSV header: {csv_header}')
    for row in csvreader:
        Ballot_Id.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])
        t_votes = (len(Ballot_Id))

# calculating votes
    for candidate in candidates:
        if candidate == "Charles Casper Stockham":
            Charles.append(candidates)
            Charles_votes = len(Charles)
        elif candidate == "Diana DeGett":
            Diana.append(candidates)
            Diana_votes = len(Diana)
        else: 
        Raymon.append(candidates)
        Raymon_votes = len(Raymon)
        

#calulating voting percentage  
Charles_percent = round(((Charles_votes / t_votes) * 100), 2)
Diana_percent = round(((Diana_votes / t_votes) * 100), 2)
Raymon_percent = round(((Raymon_votes / t_votes) * 100), 2)

#calculating winner
if Charles_percent > max(Diana_percent, Raymon_percent):
    winner = "Charles Casper Stockham"
elif Diana_percent > max(Charles_percent, Raymon_percent):
    winner = "Diana DeGett"
else:
    winner = "Raymon Anthony Doane"



print('Election Results')
print('-----------------------------------------------------')
print(f'Total Votes : {t_votes}')
print('-----------------------------------------------------')
print(f'Charles Casper Stockham: {Charles_percent}% ({Charles_votes})')
print(f'Diana DeGett: {Diana_percent}% ({Diana_votes})')
print(f'Raymon Anthony Doane: {Raymon_percent}% ({Raymon_votes})')
print('-----------------------------------------------------')
print(f"Winner: {winner}")
print('-----------------------------------------------------')


Output_path = os.path.join("..","..", "Python-Challenge", "Pybank", "resources", "election_data.txt")
with open(Output_path, 'w') as textfile:

    textfile.write('Election Results')
    textfile.write('-----------------------------------------------------')
    textfile.write(f'Total Votes : {t_votes}')
    textfile.write('-----------------------------------------------------')
    textfile.write(f'Charles Casper Stockham: {Charles_percent}% ({Charles_votes})')
    textfile.write(f'Diana DeGett: {Diana_percent}% ({Diana_votes})')
    textfile.write(f'Raymon Anthony Doane: {Raymon_percent}% ({Raymon_votes})')
    textfile.write('-----------------------------------------------------')
    textfile.write(f"Winner: {winner}")