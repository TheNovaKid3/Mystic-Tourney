import pickle
class Move:
	def __init__(self, name = None, stren = None, des = None, se = None):
		self._name = name
		self._strength = stren
		self._des = des
		self._se = se
	
	def __str__(self):
		result = self._name.strip() + ':	Strength: ' + str(self._strength) + ' \n'
		result += '	' + self._des
		return result
		
	def getName(self):
		return self._name
	
	def getStrength(self):
		return self._strength
	
	def getDes(self):
		return self._des
	
	def getSE(self):
		return self._se
	
class Set:
	def __init__(self,fileName = None):
		self._moveSet=[]
		self.fileName = fileName
		if fileName != None:
			fileObj = open(fileName, 'rb')
			while True:
				try:
					move = pickle.load(fileObj)
					self.add(move)
				except(EOFError):
					fileObj.close()
					break
					
	def __str__(self):
		result = 'Moves: \n'
		for count in range(len(self._moveSet)):
			result += '	' + self._moveSet[count].__str__() + '\n'
		return result
	
	def add(self, move):
		self._moveSet.append(move)
		
	def getMove(self, n):
		return self._moveSet[n]
					
	def save(self, fileName = None):
		if fileName != None:
			self.fileName = fileName
		elif self.fileName == None:
			return
		fileObj = open(self.fileName, 'wb')
		for move in self._moveSet:
			pickle.dump(move, fileObj)
		fileObj.close()
def newFighterMoveset():
	s = Set()
	f = open("K.txt", 'r')
	for count in range(6):
		n = f.readline()
		stren = int(f.readline())
		des = f.readline()
		se = int(f.readline())
		m = Move(n,stren,des,se)
		s.add(m)
	s.save("01001011.txt")
	s = Set()
	f = open("D.txt", 'r')
	for count in range(6):
		n = f.readline()
		stren = int(f.readline())
		des = f.readline()
		se = int(f.readline())
		m = Move(n,stren,des,se)
		s.add(m)
	s.save("01000100.txt")
	s = Set()
	f = open("V.txt", 'r')
	for count in range(6):
		n = f.readline()
		stren = int(f.readline())
		des = f.readline()
		se = int(f.readline())
		m = Move(n,stren,des,se)
		s.add(m)
	s.save("01010110.txt")
	s = Set()
	f = open("F.txt", 'r')
	for count in range(6):
		n = f.readline()
		stren = int(f.readline())
		des = f.readline()
		se = int(f.readline())
		m = Move(n,stren,des,se)
		s.add(m)
	s.save("01000110.txt")
	s = Set()
	f = open("U.txt", 'r')
	for count in range(6):
		n = f.readline()
		stren = int(f.readline())
		des = f.readline()
		se = int(f.readline())
		m = Move(n,stren,des,se)
		s.add(m)
	s.save("01010101.txt")
def test():
	s = Set("01001011.txt")
	print("Kanade")
	print(s.__str__())
	s = Set("01000100.txt")
	print("Siegfried")
	print(s.__str__())
	s = Set("01010111.txt")
	print("Alice")
	print(s.__str__())
	s = Set("01010110.txt")
	print("Rupert Scarlet")
	print(s.__str__())
	s = Set("01000110.txt")
	print("Daiyousei")
	print(s.__str__())
	s = Set("01010101.txt")
	print("Lena")
	print(s.__str__())
#newFighterMoveset()
#test()