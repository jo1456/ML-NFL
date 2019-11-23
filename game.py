from team import team
import requests as r
import bs4 as bs

class game:
	teamAbriviations = {"Philadelphia Eagles" : "phi",
	"Houston Texans" : "htx",
	"New England Patriots"  : "nwe",
	"New Orleans Saints" : "nor",
	"Arizona Cardinals" : "crd",
	"Los Angeles Chargers" : "sdg",
	"San Diego Chargers" : "sdg",
	"Cincinnati Bengals" : "cin",
	"Baltimore Ravens" : "rav",
	"Oakland Raiders" : "rai",
	"Los Angeles Rams" : "ram",
	"St. Louis Rams" : "ram",
	"Dallas Cowboys" : "dal",
	"Indianapolis Colts" : "clt",
	"San Francisco 49ers" : "sfo",
	"Kansas City Chiefs" : "kan",
	"Minnesota Vikings" : "min",
	"Seattle Seahawks" : "sea",
	"New York Giants" : "nyg",
	"Atlanta Falcons" : "atl",
	"Detroit Lions" : "det",
	"Green Bay Packers" : "gnb",
	"Jacksonville Jaguars" : "jax",
	"Tampa Bay Buccaneers" : "tam",
	"Tennessee Titans" : "oti",
	"Buffalo Bills" : "buf",
	"Chicago Bears" : "chi",
	"Pittsburgh Steelers" : "pit",
	"Denver Broncos" : "den",
	"Carolina Panthers" : "car",
	"Miami Dolphins" : "mia",
	"Cleveland Browns" : "cle",
	"Washington Redskins" : "was",
	"New York Jets" : "nyj" }
	def __init__(self, t1, t2, t1s, t2s, y, d):
		self.home = t1
		self.away = t2
		self.homeScore = t1s
		self.awayScore = t2s
		self.year = y
		self.line = 0
		self.overUnder = 0
		self.date = d

	def toList(self):
		return [self.home, self.away, self.year]
	
	def getOdds(self):
		link = "https://www.pro-football-reference.com/boxscores/" + str(self.date)+ "0" + self.teamAbriviations[self.home] + ".htm"
		page = r.get(link)
		soup = bs.BeautifulSoup(page.content, "html.parser")
		temp = soup.findAll('div', attrs={"class":"table_wrapper"})
		table = str(list(temp)[1]).replace("<!--", "").replace("-->", "")
		soup2 = bs.BeautifulSoup(table, "html.parser")
		temp2 = soup2.find_all('td')
		tempList = list(temp2) 
		#line
		lineInfo = tempList[len(tempList)-2].text.split("-") 
		print(lineInfo)
		favorite = lineInfo[0]
		if len(lineInfo) >= 2:
			if(self.home == favorite):
				self.line -= float(lineInfo[1])
			else:
				self.line += float(lineInfo[1])

		#total
		self.overUnder = float(tempList[len(tempList)-1].text.split(" ")[0]) 
