class generalDefense:
    def __init__(self, Fum, Ints, PenaltyYards, Pen1ds):
        self.fum = Fum
        self.ints = Ints
        self.penaltyYards = PenaltyYards
        self.pen1ds = Pen1ds

    def getList(self):
        return [self.fum,
        self.ints,
        self.penaltyYards,
        self.pen1ds]