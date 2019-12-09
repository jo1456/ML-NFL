class driveAvgs:
    def __init__(self, NumberOfDrives, Plays, ScorePercent, ToPercent, PlaysPerDrive, YardsPerDrive, Start, Time, PtsPerDrive):
        self.numberOfDrives = NumberOfDrives
        self.plays = Plays
        self.scorePercent = ScorePercent
        self.toPercent = ToPercent
        self.playsPerDrive = PlaysPerDrive
        self.yardsPerDrive = YardsPerDrive
        self.start = Start
        self.time = Time
        self.ptsPerDrive = PtsPerDrive

    def getList(self):
        return [str(self.numberOfDrives), str(self.plays), str(self.scorePercent), str(self.toPercent),
              str(self.playsPerDrive), str(self.yardsPerDrive), str(self.start)
             , str(self.time), str(self.ptsPerDrive)]
