class player:
    def __init__(self, ign, claimedTier):
        self.ign = ign
        self.claimedTier = claimedTier

    def __str__(self) -> str:
        return(self.ign + "\t | signed up for tier: "+str(self.claimedTier))