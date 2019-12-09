class kickReturns:
   def __init__(self, Punt, Kick):
       self.puntYards = Punt
       self.kickYards = Kick

   def getList(self):
        return [str(self.puntYards) , str(self.kickYards)]
   
