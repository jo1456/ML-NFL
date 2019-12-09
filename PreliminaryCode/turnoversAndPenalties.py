class generalDefense:
    def __init__(self, Fum, Ints, PenaltyYards, Pen1ds, ScorePct, ToPct):
        self.fum = Fum
        self.ints = Ints
        self.penaltyYards = PenaltyYards
        self.pen1ds = Pen1ds
        self.scorePct = ScorePct
        self.toPct = ToPct

    def getList(self):
        return [self.fum,
        self.ints,
        self.penaltyYards,
        self.pen1ds,
        self.scorePct,
        self.toPct]
