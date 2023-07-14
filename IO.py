import csv
import player

def strToTier(s):
    if s == "Tier 2 (plat 1 and below)":
        return 2
    else: 
        return 1

def teamStrToList(s):
    s = s.split(",")
    retVal = []
    for item in s:
        if item[0]== ' ':
            item = item[1:]
        if item[-1] == ' ':
            item = item[:-1]
        retVal.append(item)
    return retVal

def input(filename):
    players = []
    with open(filename, newline = '') as csvfile:
        rows = csv.reader(csvfile, delimiter= ',')
        #dont read the header row
        first = True
        for row in rows:
            #change first to false to bypass block and begin reading
            if first:
                first=False
                continue
            for person in teamStrToList(row[7]):
                players.append(player.player(person,strToTier(row[2])))
    return players
            
def output(filename, names, tiers, validity):
    header = ["IGN","Claimed Tier", "Valid Tier (T/F)"]
    all = header + names + tiers + validity
    with open(filename, 'w') as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow(header)

        for i in range(len(names)):
            row = [names[i],tiers[i],validity[i]]
            writer.writerow(row)
    


