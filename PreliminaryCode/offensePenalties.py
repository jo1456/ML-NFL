class offensePenalties:
    def __init__(self, PenaltyYards, Pen1ds):
        self.penaltyYards = PenaltyYards
        self.pen1ds = Pen1ds

    def getList(self):
        return [
        self.penaltyYards,
        self.pen1ds]
