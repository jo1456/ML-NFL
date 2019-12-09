from driveAvgs import driveAvgs
from rushingOff import rushingOff
from passingOff import passingOff
from kicking import kicking
from kickReturns import kickReturns
from conversions import conversions
from passingDefense import passingDefense
from offensePenalties import offensePenalties
import numpy as np

class team:
    def __int__(self):
        self.name = ""
        self.year = ""
        self.DriveAvgs = driveAvgs(0,0,0,0,0,0,0,0,0)
        self.Conversions = conversions(0,0,0,0,0,0,0)
        self.Kicking = kicking(0, 0, 0)
        self.KickReturns = kickReturns(0, 0)
        self.RushingOff = rushingOff(0, 0, 0, 0, 0, 0, 0)
        self.PassingOff = passingOff(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.DriveAvgsAgainst = driveAvgs(0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.ConversionsAgainst = conversions(0, 0, 0, 0, 0, 0, 0)
        self.KickingAgainst = kicking(0, 0, 0)
        self.KickReturnsAgainst = kickReturns(0, 0)
        self.RushingOffAgainst = rushingOff(0, 0, 0, 0, 0, 0, 0)
        self.PassingDefense = passingOff(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.GeneralDefense = generalDefense(0,0,0,0)
        self.OffensePenalties = offensePenalties(0,0)

    def setDriveAvgs(self, dAvgs):
        self.DriveAvgs = dAvgs

    def setConversions(self, cons):
        self.Conversions = cons

    def setKicking(self, kick):
        self.Kicking = kick

    def setKickReturns(self, dAvgs):
        self.KickReturns = dAvgs

    def setRushingOff(self, dAvgs):
        self.RushingOff = dAvgs

    def setPassingOff(self, dAvgs):
        self.PassingOff = dAvgs

    def setDriveAvgsAgainst(self, dAvgs):
        self.DriveAvgsAgainst = dAvgs

    def setConversionsAgainst(self, dAvgs):
        self.ConversionsAgainst = dAvgs

    def setKickingAgainst(self, dAvgs):
        self.KickingAgainst = dAvgs

    def setKickReturnsAgainst(self, dAvgs):
        self.KickReturnsAgainst = dAvgs

    def setRushingOffAgainst(self, dAvgs):
        self.RushingOffAgainst = dAvgs

    def setPassingDefense(self, dAvgs):
        self.PassingDefense = dAvgs

    def setGeneralDefense(self, dAvgs):
        self.GeneralDefense = dAvgs

    def setOffensePenalties(self, dAvgs):
        self.OffensePenalties = dAvgs

    def getDriveAvgs(self):
        return self.DriveAvgs

    def getConversions(self):
        return self.Conversions

    def getKicking(self):
        return self.Kicking

    def getKickReturns(self):
        return self.KickReturns

    def getRushingOff(self):
        return self.RushingOff

    def getPassingOff(self):
        return self.PassingOff

    def getDriveAvgsAgainst(self):
        return self.DriveAvgsAgainst

    def getConversionsAgainst(self):
        return self.ConversionsAgainst

    def getKickingAgainst(self):
        return self.KickingAgainst

    def getKickReturnsAgainst(self):
        return self.KickReturnsAgainst

    def getRushingOffAgainst(self):
        return self.RushingOffAgainst

    def getPassingDefense(self):
        return self.PassingOffAgainst

    def getGeneralDefense(self):
        return self.GeneralDefense

    def getOffensePenalties(self):
        return self.OffensePenalties

    def printTeam(self):
        print(self.Conversions.getList())

def create_row(offense, defense, score):
    row = [offense.name]
    print(row)
    #row += (np.array(offense.getDriveAvgs().getList()) + np.array(defense.getDriveAvgsAgainst().getList()))/2
    #row += (np.array(offense.getConversions().getList()) + np.array(defense.getConversionsAgainst().getList()))/2
    #row += (np.array(offense.getKicking().getList()) + np.array(defense.getKickingAgainst().getList()))/2
    #row +=(np.array(offense.getKickReturns().getList()) + np.array(defense.getKickReturnsAgainst().getList()))/2
    #row += (np.array(offense.getRushingOff().getList()) + np.array(defense.getRushingOffAgainst().getList()))/2
    #row += np.array(offense.getPassingOff().getList())
    #row += np.array(defense.getPassingDefense().getList())
    #row += np.array(defense.getGeneralDefense().getList()[0:2])
    #row += (np.array(defense.getGeneralDefense().getList()[2:4])+np.array(offense.getOffensePenalties().getList()))/2
    #row += [score]



