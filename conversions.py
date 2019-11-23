class conversions:
   def __init__(self, ThirdPct, FourthAttempts, FourthConversions, FourthPct, RdAttempts, RdTds, RdPct):
        self.thirdPct = ThirdPct
        self.fourthAttempts = FourthAttempts
        self.fourthConversions = FourthConversions
        self.fourthPct = FourthPct
        self.rdAttemtps = RdAttempts
        self.rdTds = RdTds
        self.rdPct = RdPct

   def getList(self):
        return [str(self.thirdPct), str(self.fourthAttempts), str(self.fourthConversions), str(self.fourthPct),
              str(self.rdAttemtps), str(self.rdTds), str(self.rdPct)]