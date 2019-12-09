class kicking:
	def __init__(self, FgPct, XpPct, YardsPerPunt):
		self.fgPct = FgPct
		self.xpPct = XpPct
		self.yardsPerPunt = YardsPerPunt

	def getList(self):
		return [str(self.fgPct), str(self.xpPct), str(self.yardsPerPunt)]
