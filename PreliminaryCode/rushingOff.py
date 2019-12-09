class rushingOff:
   def __init__(self, Attempts, Yards, Tds, YardsPerCarry, YardsPerGame, Fumbles, PointsFromRush):
        self.attempts = Attempts
        self.yards = Yards
        self.tds = Tds
        self.yardsPerCarry = YardsPerCarry
        self.yardsPerGame = YardsPerGame
        self.fumbles = Fumbles
        self.pointsFromRush = PointsFromRush

   def getList(self):
        return [str(self.attempts) , str(self.yards) , str(self.tds) , str(self.yardsPerCarry) ,
              str(self.yardsPerGame) , str(self.fumbles) , str(self.pointsFromRush)]
