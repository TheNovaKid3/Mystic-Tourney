class Fighter(object):
	def __init__(self, fileName):
		"""Creates a Fighter object"""
		f = open(fileName, 'r')
		a = f.readline()
		a = a.strip()
		self._name = a
		a = f.readline()
		a = a.strip()
		self._atk = int(a)
		self._a = self._atk
		a = f.readline()
		a = a.strip()
		self._den = int(a)
		self._b = self._den
		a = f.readline()
		a = a.strip()
		self._acc = int(a)
		self._c = self._acc
		a = f.readline()
		a = a.strip()
		self._dex = int(a)
		self._d = self._dex
		a = f.readline()
		a = a.strip()
		self._agi = int(a)
		self._e = self._agi
		a = f.readline()
		a = a.strip()
		self._sta = int(a)
		a = f.readline()
		self._pin = a.strip()
		self._HP = (6*(self._sta)*20)
		self._MAXHP = self._HP
		self._buff = 0
		self._status = 0
		self._turn = 0
		self._percent = 0
		self._sigma = 0
	
	def __str__(self):
		"""Returns the string form of a fighter Object"""
		a = str(self._HP) + '/' + str(self._MAXHP)
		a = a.strip()
		result = self._name+ ': HP: ' + a + '\n'
		result += '	Attack: ' + str(self._atk) + '	Defense: ' + str(self._den) + ' \n'
		result += '	Accuracy: ' + str(self._acc) + '	Dexterity: ' + str(self._dex) + ' \n'
		result += '	Agility: ' + str(self._agi) + '	Stamina: ' + str(self._sta)
		return result
	
	def getName(self):
		"""Returns the name of a Fighter"""
		return self._name
		
	def getAtk(self):
		"""Returns the Attack of a Fighter"""
		return self._atk
		
	def getDefense(self):
		"""Returns the Defense of a Fighter"""
		return self._den
			
	def getAcc(self):
		"""Returns the Accuracy of a Fighter"""
		return self._acc
			
	def getDex(self):
		"""Returns the Dexterity of a Fighter"""
		return self._dex
			
	def getAgi(self):
		"""Returns the Agility of a Fighter"""
		return self._agi
		
	def getSta(self):
		"""Returns the Attack of a Fighter"""
		return self._sta
		
	def getPin(self):
		"""Returns the Pin of a Fighter"""
		return self._pin
		
	def getHP(self):
		"""Returns the HP of a Fighter"""
		return self._HP
		
	def takeDamage(self, damage):
		self._HP -= int(damage)
		while self._HP < 0:
			self._HP += 1
		
	def heal(self, heal):
		self._HP += heal
		if self._HP > self._MAXHP:
			self._HP = self._MAXHP
		return
		
	def getMAXHP(self):
		"""Returns the HP of a Fighter"""
		return self._MAXHP
		
	def getBuff(self):
		"""Returns the Number indicating which buff the Fighter has. 0 indicates none"""
		return self._buff
		
	def setBuff(self, buffNum):
		self._buff = buffNum
		return
		
	def buffFighter(self):
		a = self.getBuff()
		if a != 0:
			if a == 1:
				self._atk += 1
				self.setBuff(0)
			elif a == 2:
				self._den += 1
				self.setBuff(0)
			elif a == 3:
				self._acc += 1
				self.setBuff(0)
			elif a == 4:
				self._dex += 1
				self.setBuff(0)
			elif a == 5:
				self._agi += 1
				self.setBuff(0)
		else:
			self._atk = self._a
			self._den = self._b
			self._acc = self._c
			self._dex = self._d
			self._agi = self._e
		return
		
	def getStatus(self):
		"""Returns the Number indicating the Status of the Fighter. 0 indicates none."""
		return self._status
	
	def setStatus(self, statusNum):
		self._status = statusNum
		if statusNum == 1 or statusNum == 3 or statusNum == 4:
			self.setTurn(5)
		elif statusNum == 2:
			self.setPercent(100)
		elif statusNum == 5:
			self.setPercent(100)
		return
		
	def getTurn(self):
		return self._turn
	
	def setTurn(self, new):
		self._turn = new
		return
		
	def getPercent(self):
		return self._percent
	
	def setPercent(self, new):
		self._percent = new
		return
	
def test():
	f = Fighter("kitsune.txt")
	print(f.__str__())
	f = Fighter("dragon.txt")
	print(f.__str__())
	f = Fighter("witch.txt")
	print(f.__str__())
	f = Fighter("vampire.txt")
	print(f.__str__())
	f = Fighter("fairy.txt")
	print(f.__str__())
	f = Fighter("unicorn.txt")
	print(f.__str__())
#test()