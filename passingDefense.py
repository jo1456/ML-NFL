class passingDefense:
    def __init__(self, Attempted, Completed, CompPct, Yds, Td, Dadot, Air, Yac, Blitz, BlitzPct, Hurry, HurryPct,
                QBkd, QBkdPct, Sacks, Pressure, PressurePct, MissedTackles):
        self.attempted = Attempted
        self.completed = Completed
        self.yds = Yds
        self.td = Td
        self.dadot = Dadot
        self.air = Air
        self.yac = Yac
        self.blitz = Blitz
        self.blitzPct = BlitzPct
        self.hurry = Hurry
        self.hurryPct = HurryPct
        self.qbkd = QBkd
        self.qbkdPct = QBkdPct
        self.sacks = Sacks
        self.pressure = Pressure
        self.pressurePct = PressurePct
        self.missedTackles = MissedTackles

    def getList(self):
        return [self.attempted, 
        self.completed,
        self.yds,
        self.td,
        self.dadot,
        self.air,
        self.yac,
        self.blitz,
        self.blitzPct,
        self.hurry,
        self.hurryPct,
        self.qbkd,
        self.qbkdPct,
        self.sacks,
        self.pressure,
        self.pressurePct,
        self.missedTackles]