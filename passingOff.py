class passingOff:
    def __init__(self, Completed, Attempted, CompPct, Yds, Td, TdPct, Int, IntPct,
                 YardsPerAttempt, YardsPerGame, Qbr,
                 Sacks, YardsLostSacks, NetYardsPerPassAttempt, AdjustedNetYardsPerPassAttempt,
                 SackRate, Comebacks, GameWinningDrives, PointsFromPassing):
        self.completed = Completed
        self.attempted = Attempted
        self.compPct = CompPct
        self.yds = Yds
        self.td = Td
        self.tdPct = TdPct
        self.ints = Int
        self.intPct = IntPct
        self.yardsPerAttempt = YardsPerAttempt
        self.yardsPerGame = YardsPerGame
        self.qbr = Qbr
        self.sacks = Sacks
        self.yardsLostDueToSacks = YardsLostSacks
        self.netYardsPerPassAttempt = NetYardsPerPassAttempt
        self.adjustedNetYardsPerPassAttempt = AdjustedNetYardsPerPassAttempt
        self.sackRate = SackRate
        self.comebacks = Comebacks
        self.gameWinningDrives = GameWinningDrives
        self.pointsFromPassing = PointsFromPassing

    def getList(self):
        return [self.completed,
        self.attempted,
        self.compPct,
        self.yds,
        self.td ,
        self.tdPct,
        self.ints ,
        self.intPct,
        self.yardsPerAttempt, 
        self.yardsPerGame ,
        self.qbr ,
        self.sacks, 
        self.yardsLostDueToSacks ,
        self.netYardsPerPassAttempt, 
        self.adjustedNetYardsPerPassAttempt, 
        self.sackRate ,
        self.comebacks,
        self.gameWinningDrives,
        self.pointsFromPassing ]