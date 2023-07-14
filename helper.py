ranks = ["Iron ","Iron ", "Iron ", 
"Bronze ","Bronze ","Bronze ",
"Silver ","Silver ","Silver ",
"Gold ","Gold ","Gold ",
"Platinum ","Platinum ","Platinum ",
"Diamond ","Diamond ","Diamond ",
"Ascendant", "Ascendant", "Ascendant", 
"Immortal ","Immortal ","Immortal ",
]
t2 = ['Iron 1', 'Iron 2', 'Iron 3', 'Bronze 1', 'Bronze 2', 'Bronze 3', 'Silver 1', 'Silver 2', 'Silver 3', 'Gold 1', 'Gold 2', 'Gold 3', 'Platinum 1']

for i in range(len(ranks)):
    ranks[i]=ranks[i] + str((i%3)+1)
ranks.append("Radiant")


#---------------------------------------------------------------------------------------------

def validRank(text):
    return (text in ranks or text.endswith("RR") )


def validTier(strrank, tier:int):
    if not tier in [1,2]:
        return False
    return ((tier == 2 and strrank in t2) or (tier == 1 and not strrank in t2))

#takes list of episode 4 ranks and finds the appropriate tier
def ranksToTier(E4Ranks):
    t2 = True

    print(E4Ranks)
    ERRORCOUNT = 0
    for actrank in E4Ranks:
        if ("ERROR" in actrank):
            ERRORCOUNT+=1
        elif not (validTier(actrank, 2)):
            t2 = False
    
    if ERRORCOUNT > 0:
        return 3
    
    if t2:
        return 2
    return 1



