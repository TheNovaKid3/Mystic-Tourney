from tkinter import *
from fighter import Fighter
from moveset import Set, Move
import tkinter.messagebox
import random
class mainMenu(Frame):
	
	def __init__(self):
		Frame.__init__(self)
		self.master.title("Mystic Tourney")
		self.master.rowconfigure(0, weight = 1)
		self.master.columnconfigure(0, weight = 1)
		self.grid(sticky = W+E+N+S)
		titleFont = ("Verdana", 20)
		self._mainTitle = Label(self, text = "Mystic Tourney", font = titleFont)
		self._mainTitle.grid(row = 0, column = 1)
		self._option1 = Button(self, text = "One Player", command = self._characterSelect)
		self._option1.grid(row = 1)
		self._option1 = Button(self, text = "Two Player", command = self._characterSelect2)
		self._option1.grid(row = 1,column = 2)
		self._option1 = Button(self, text = "Quit", command = self._quit)
		self._option1.grid(row = 2,column = 1)
		
	def _characterSelect(self):
		secondPlayer = False
		self.destroy()
		CharaSelect(secondPlayer).mainloop()
	def _characterSelect2(self):
		secondPlayer = True
		self.destroy()
		CharaSelect(secondPlayer).mainloop()
	def _quit(self):
		t = tkinter.messagebox.askyesno(title = "Mystic Tourney", message = "Do you really want to quit?")
		if t == True:
			self.master.destroy()
		

class CharaSelect(Frame):
	
	def __init__(self, player2):
		Frame.__init__(self)
		self._player2 = player2
		self.master.title("Mystic Tourney")
		self.master.rowconfigure(0, weight = 1)
		self.master.columnconfigure(0, weight = 1)
		self.grid(sticky = W+E+N+S)
		self._x = 0
		self._y = 0
		self._fighters1List =[]
		self._fighters2List = []
		f1 = Fighter("kitsune.txt")
		f2 = Fighter("kitsune.txt")
		self._fighters1List.append(f1)
		self._fighters2List.append(f2)
		f1 = Fighter("dragon.txt")
		f2 = Fighter("dragon.txt")
		self._fighters1List.append(f1)
		self._fighters2List.append(f2)
		f1 = Fighter("witch.txt")
		f2 = Fighter("witch.txt")
		self._fighters1List.append(f1)
		self._fighters2List.append(f2)
		f1 = Fighter("vampire.txt")
		f2 = Fighter("vampire.txt")
		self._fighters1List.append(f1)
		self._fighters2List.append(f2)
		f1 = Fighter("fairy.txt")
		f2 = Fighter("fairy.txt")
		self._fighters1List.append(f1)
		self._fighters2List.append(f2)
		f1 = Fighter("unicorn.txt")
		f2 = Fighter("unicorn.txt")
		self._fighters1List.append(f1)
		self._fighters2List.append(f2)
		self._fighter1 = Button(self, text = self._fighters1List[0].getName(), command = self._chooseCharacter1)
		self._fighter1.grid(row = 0)
		self._Blank = Label(self, text = "-----------")
		self._Blank.grid(row = 1)
		self._fighter2 = Button(self, text = self._fighters1List[1].getName(), command = self._chooseCharacter2)
		self._fighter2.grid(row = 2)
		self._Blank = Label(self, text = "-----------")
		self._Blank.grid(row = 3)
		self._fighter3 = Button(self, text = self._fighters1List[2].getName(), command = self._chooseCharacter3)
		self._fighter3.grid(row = 4)
		self._Blank = Label(self, text = "-----------")
		self._Blank.grid(row = 5)
		self._fighter4 = Button(self, text = self._fighters1List[3].getName(), command = self._chooseCharacter4)
		self._fighter4.grid(row = 0, column = 2)
		self._Blank = Label(self, text = "-----------")
		self._Blank.grid(row = 1, column = 2)
		self._fighter5 = Button(self, text = self._fighters1List[4].getName(), command = self._chooseCharacter5)
		self._fighter5.grid(row = 2, column = 2)
		self._Blank = Label(self, text = "-----------")
		self._Blank.grid(row = 3, column = 2)
		self._fighter6 = Button(self, text = self._fighters1List[5].getName(), command = self._chooseCharacter6)
		self._fighter6.grid(row = 4, column = 2)
		self._fighterr = Button(self, text = "Random", command = self._chooseCharacterR)
		self._fighterr.grid(row = 6, column = 0)
		self._chooseChara = Label(self, text = "Choose Fighters")
		self._chooseChara.grid(row = 7, column = 1)
			
	def _chooseCharacter1(self):
		fNum = 0
		if self._x == 0:
			self._playFighter1 = self._fighters1List[fNum]
			self._x += 1
			self._Chara = Label(self, text = "Player 1 selected " + self._playFighter1.getName())
			self._Chara.grid(row = 8, column = 1)
		else:
			self._playFighter2 = self._fighters2List[fNum]
			if self._player2 == True:
				p = "Player 2"
			else: 
				p = "Opponent"
			t = "Player 1 selected " + self._playFighter1.getName() + "\n" + p + " selected " + self._playFighter2.getName() + "\n Is this correct?"
			if tkinter.messagebox.askyesno(title = "Mystic Tourney", message = t) == True:
				self.destroy()
				BattleScreen(self._playFighter1, self._playFighter2, self._player2)
			else:
				self.destroy()
				CharaSelect(self._player2)
	def _chooseCharacter2(self):
		fNum = 1
		if self._x == 0:
			self._playFighter1 = self._fighters1List[fNum]
			self._x += 1
			self._Chara = Label(self, text = "Player 1 selected " + self._playFighter1.getName())
			self._Chara.grid(row = 8, column = 1)
		else:
			self._playFighter2 = self._fighters2List[fNum]
			if self._player2 == True:
				p = "Player 2"
			else: 
				p = "Opponent"
			t = "Player 1 selected " + self._playFighter1.getName() + "\n" + p + " selected " + self._playFighter2.getName() + "\n Is this correct?"
			if tkinter.messagebox.askyesno(title = "Mystic Tourney", message = t) == True:
				self.destroy()
				BattleScreen(self._playFighter1, self._playFighter2, self._player2)
			else:
				self.destroy()
				CharaSelect(self._player2)
				
	def _chooseCharacter3(self):
		fNum = 2
		if self._x == 0:
			self._playFighter1 = self._fighters1List[fNum]
			self._x += 1
			self._Chara = Label(self, text = "Player 1 selected " + self._playFighter1.getName())
			self._Chara.grid(row = 8, column = 1)
		else:
			self._playFighter2 = self._fighters2List[fNum]
			if self._player2 == True:
				p = "Player 2"
			else: 
				p = "Opponent"
			t = "Player 1 selected " + self._playFighter1.getName() + "\n" + p + " selected " + self._playFighter2.getName() + "\n Is this correct?"
			if tkinter.messagebox.askyesno(title = "Mystic Tourney", message = t) == True:
				self.destroy()
				BattleScreen(self._playFighter1, self._playFighter2, self._player2)
			else:
				self.destroy()
				CharaSelect(self._player2)
		
	def _chooseCharacter4(self):
		fNum = 3
		if self._x == 0:
			self._playFighter1 = self._fighters1List[fNum]
			self._x += 1
			self._Chara = Label(self, text = "Player 1 selected " + self._playFighter1.getName())
			self._Chara.grid(row = 8, column = 1)
		else:
			self._playFighter2 = self._fighters2List[fNum]
			if self._player2 == True:
				p = "Player 2"
			else: 
				p = "Opponent"
			t = "Player 1 selected " + self._playFighter1.getName() + "\n" + p + " selected " + self._playFighter2.getName() + "\n Is this correct?"
			if tkinter.messagebox.askyesno(title = "Mystic Tourney", message = t) == True:
				self.destroy()
				BattleScreen(self._playFighter1, self._playFighter2, self._player2)
			else:
				self.destroy()
				CharaSelect(self._player2)
	def _chooseCharacter5(self):
		fNum = 4
		if self._x == 0:
			self._playFighter1 = self._fighters1List[fNum]
			self._x += 1
			self._Chara = Label(self, text = "Player 1 selected " + self._playFighter1.getName())
			self._Chara.grid(row = 8, column = 1)
		else:
			self._playFighter2 = self._fighters2List[fNum]
			if self._player2 == True:
				p = "Player 2"
			else: 
				p = "Opponent"
			t = "Player 1 selected " + self._playFighter1.getName() + "\n" + p + " selected " + self._playFighter2.getName() + "\n Is this correct?"
			if tkinter.messagebox.askyesno(title = "Mystic Tourney", message = t) == True:
				self.destroy()
				BattleScreen(self._playFighter1, self._playFighter2, self._player2)
			else:
				self.destroy()
				CharaSelect(self._player2)
	def _chooseCharacter6(self):
		fNum = 5
		if self._x == 0:
			self._playFighter1 = self._fighters1List[fNum]
			self._x += 1
			self._Chara = Label(self, text = "Player 1 selected " + self._playFighter1.getName())
			self._Chara.grid(row = 8, column = 1)
		else:
			self._playFighter2 = self._fighters2List[fNum]
			if self._player2 == True:
				p = "Player 2"
			else: 
				p = "Opponent"
			t = "Player 1 selected " + self._playFighter1.getName() + "\n" + p + " selected " + self._playFighter2.getName() + "\n Is this correct?"
			if tkinter.messagebox.askyesno(title = "Mystic Tourney", message = t) == True:
				self.destroy()
				BattleScreen(self._playFighter1, self._playFighter2, self._player2)
			else:
				self.destroy()
				CharaSelect(self._player2)
			
	def _chooseCharacterR(self):
			fNum = random.randint(0,5)
			if self._x == 0:
				self._playFighter1 = self._fighters1List[fNum]
				self._x += 1
				self._Chara = Label(self, text = "Player 1 selected" + self._playFighter1.getName())
				self._Chara.grid(row = 8, column = 1)
			else:
				self._playFighter2 = self._fighters2List[fNum]
				if self._player2 == True:
					p = "Player 2"
				else: 
					p = "Opponent"
				t = "Player 1 selected " + self._playFighter1.getName() + "\n" + p + " selected " + self._playFighter2.getName() + "\n Is this correct?"
				if tkinter.messagebox.askyesno(title = "Mystic Tourney", message = t) == True:
					self.destroy()
					BattleScreen(self._playFighter1, self._playFighter2, self._player2)
				else:
					self.destroy()
					CharaSelect(self._player2)
				
class BattleScreen(Frame):
	def __init__(self, player1, player2, secondplayer):
		"""Creating the Battle Screen"""
		Frame.__init__(self)
		self.master.title("Mystic Tourney")
		self.master.rowconfigure(0, weight = 1)
		self.master.columnconfigure(0, weight = 1)
		self.grid(sticky = W+E+N+S)
		self._player1 = player1
		self._player2 = player2
		self._secondPlayer = secondplayer
		self._sigma = 0
		self._omega = 0
		self._beta = 0
		self._x = 0
		self._y = 0
		self._play1Move = None
		self._play2Move = None
		if self._secondPlayer == True:
			t = "Player 1"
		else: 
			t = "Player"
		self._playerFrame = LabelFrame(self, text = t, padx = 5, pady = 5)
		self._playerFrame.grid(row = 0, column = 0, sticky = N+W)
		self._playerName = Label(self._playerFrame, text = self._player1.getName())
		self._playerName.grid(row = 0, sticky = W)
		self._playerHP = Label(self._playerFrame, text = (str(self._player1.getHP()) +"/" + str(self._player1.getMAXHP())))	
		self._playerHP.grid(row = 1, sticky = W)
		t = "None"
		self._playerStatus = Label(self._playerFrame, text = ("Status: " + t))
		self._playerStatus.grid(row = 2, sticky = W)
		
		#Non-Player Character or opponent
		if self._secondPlayer == True:
			t = "Player 2"
		else: 
			t = "Opponent"
		self._NPCFrame = LabelFrame(self, text = t, padx = 5 , pady = 5)
		self._NPCFrame.grid(row = 0, column = 2, sticky = N+E)
		if self._player1.getName() == self._player2.getName():
			self._player2._name += " 2"
		self._NPCName = Label(self._NPCFrame, text = self._player2.getName())
		self._NPCName.grid(row = 0 , sticky = W)
		self._NPCHP = Label(self._NPCFrame, text = (str(self._player2.getHP()) +"/" + str(self._player2.getMAXHP())))	
		self._NPCHP.grid(row = 1, sticky = W)
		t = "None"
		self._NPCStatus = Label(self._NPCFrame, text = ("Status: " + t))
		self._NPCStatus.grid(row = 2, sticky = W)
		
		#Create Move Box
		t = self._player1.getPin() + ".txt"
		t = t.strip()
		s = Set(t)
		self._play1s = s._moveSet
		if self._secondPlayer == True:
			p = "First Player's Moves"
		else:
			p = "Player"
		self._moveFrame = LabelFrame(self, text = p, padx = 5, pady = 5)
		self._moveFrame.grid(row = 1, sticky = W+S)
		self._blankLabel = Label(self._moveFrame, text = "|")
		self._move1 = Button(self._moveFrame, text = s.getMove(0).getName().strip(), command = self.inputPlay1Move1)
		self._move1.grid(row = 0)
		self._blankLabel = Label(self._moveFrame, text = "|")
		self._blankLabel.grid(row = 0, column = 1)
		self._move2 = Button(self._moveFrame, text = s.getMove(1).getName().strip(), command = self.inputPlay1Move2)
		self._move2.grid(row = 0, column = 2)
		self._blankLabel = Label(self._moveFrame, text = "-----")
		self._blankLabel.grid(row = 1)
		self._blankLabel = Label(self._moveFrame, text = "-----")
		self._blankLabel.grid(row = 1, column = 1)
		self._blankLabel = Label(self._moveFrame, text = "-----")
		self._blankLabel.grid(row = 1, column = 2)
		self._move3 = Button(self._moveFrame, text = s.getMove(2).getName().strip(), command = self.inputPlay1Move3)
		self._move3.grid(row = 2)
		self._blankLabel = Label(self._moveFrame, text = "|")
		self._blankLabel.grid(row = 2, column = 1)
		self._move4 = Button(self._moveFrame, text = s.getMove(3).getName().strip(), command = self.inputPlay1Move4)
		self._move4.grid(row = 2, column = 2)
		self._blankLabel = Label(self._moveFrame, text = "-----")
		self._blankLabel.grid(row = 3)
		self._blankLabel = Label(self._moveFrame, text = "-----")
		self._blankLabel.grid(row = 3, column = 1)
		self._blankLabel = Label(self._moveFrame, text = "-----")
		self._blankLabel.grid(row = 3, column = 2)
		self._move5 = Button(self._moveFrame, text = s.getMove(4).getName().strip(), command = self.inputPlay1Move5)
		self._move5.grid(row = 4)
		self._blankLabel = Label(self._moveFrame, text = "|")
		self._blankLabel.grid(row = 4, column = 1)
		self._move6 = Button(self._moveFrame, text = s.getMove(5).getName().strip(), command = self.inputPlay1Move6)
		self._move6.grid(row = 4, column = 2)
		
		if self._secondPlayer == True:
			t = self._player2.getPin() + ".txt"
			t = t.strip()
			s = Set(t)
			self._play2s = s._moveSet
			self._moveFrame = LabelFrame(self, text = "Second Player's Moves", padx = 5, pady = 5)
			self._moveFrame.grid(row = 1, column = 2, sticky = E)
			self._blankLabel = Label(self._moveFrame, text = "|")
			self._move1 = Button(self._moveFrame, text = s.getMove(0).getName().strip(), command = self.inputPlay2Move1)
			self._move1.grid(row = 0)
			self._blankLabel = Label(self._moveFrame, text = "|")
			self._blankLabel.grid(row = 0, column = 1)
			self._move2 = Button(self._moveFrame, text = s.getMove(1).getName().strip(), command = self.inputPlay2Move2)
			self._move2.grid(row = 0, column = 2)
			self._blankLabel = Label(self._moveFrame, text = "-------")
			self._blankLabel.grid(row = 1)
			self._blankLabel = Label(self._moveFrame, text = "-------")
			self._blankLabel.grid(row = 1, column = 1)
			self._blankLabel = Label(self._moveFrame, text = "-------")
			self._blankLabel.grid(row = 1, column = 2)
			self._move3 = Button(self._moveFrame, text = s.getMove(2).getName().strip(), command = self.inputPlay2Move3)
			self._move3.grid(row = 2)
			self._blankLabel = Label(self._moveFrame, text = "|")
			self._blankLabel.grid(row = 2, column = 1)
			self._move4 = Button(self._moveFrame, text = s.getMove(3).getName().strip(), command = self.inputPlay2Move4)
			self._move4.grid(row = 2, column = 2)
			self._blankLabel = Label(self._moveFrame, text = "-------")
			self._blankLabel.grid(row = 3)
			self._blankLabel = Label(self._moveFrame, text = "-------")
			self._blankLabel.grid(row = 3, column = 1)
			self._blankLabel = Label(self._moveFrame, text = "-------")
			self._blankLabel.grid(row = 3, column = 2)
			self._move5 = Button(self._moveFrame, text = s.getMove(4).getName().strip(), command = self.inputPlay2Move5)
			self._move5.grid(row = 4)
			self._blankLabel = Label(self._moveFrame, text = "|")
			self._blankLabel.grid(row = 4, column = 1)
			self._move6 = Button(self._moveFrame, text = s.getMove(5).getName().strip(), command = self.inputPlay2Move6)
			self._move6.grid(row = 4, column = 2)
		
		#Create List Dialouge box
		self._listPane = Frame(self)
		self._listPane.grid(row = 2, column = 1, sticky = S)
		self._yScroll = Scrollbar(self._listPane, orient = VERTICAL)
		self._yScroll.grid(row = 2, column = 1, sticky = S)
		self._theList = Listbox(self._listPane, width = 50, height = 10, yscrollcommand = self._yScroll.set)
		self._theList.grid(row = 2, column = 1, sticky = S)
		self._clearButton = Button(self,
								text = "Clear Messages",
								command = self._remove)
		self._clearButton.grid(row = 3, column = 1, sticky = S)
						
	def _displayMessage(self, string):
		"""Displays string in message box"""
		self._theList.insert(END, string)
		self._theList.see(END)
	
	def _remove(self):
		"""Removes all Items in list"""
		while self._theList.size() > 0:
			self._theList.delete(END)
	
	def turnCalc(self, Agi1, Agi2):
		"""Returns true if fighter1 goes first, returns false if fighter2 goes"""
		r1 = random.randint(1,5)
		r2 = random.randint(1,5)
		if Agi1 * r1 >= Agi2 * r2:
			return True
		else:
			return False
		
	def atkHitCalc(self, atkFighterAcc, defFighterDex):
		"""Determines if an attack hit the target. Returns true if yes, retuns false if no."""
		dex = defFighterDex
		if atkFighterAcc > 3:
			dex -= (atkFighterAcc-3)
			while dex < 0:
				dex += 1
		if atkFighterAcc < 3:
			dex -= (atkFighterAcc-3)
		r = random.randint(1,100)
		if r >= (dex*10):
			return True
		else:
			return False

	def damageCalculation(self, Atk, Den, MoveStr):
		"""Returns the damage done to a Fighter"""
		r = random.randint(1,10)
		if r == 10:
			return ((Atk * MoveStr)*20)/(Den * 2)
		else:
			return ((Atk * MoveStr)*10)/(Den * 2)
	
	def inputPlay1Move1(self):
		if self._x == 0:
			self._play1Move = self._play1s[0]
			self._x = 1
		if self._secondPlayer == True:
			if self._y != 0:
				self.fullTurn()
			else:
				self._displayMessage("Waiting for Second Player.")
				return
		else:
			self.fullTurn()
	def inputPlay1Move2(self):
		if self._x == 0:
			self._play1Move = self._play1s[1]
			self._x = 1
		if self._secondPlayer == True:
			if self._y != 0:
				self.fullTurn()
			else:
				self._displayMessage("Waiting for Second Player.")
				return
		else:
			self.fullTurn()
	def inputPlay1Move3(self):
		if self._x == 0:
			self._play1Move = self._play1s[2]
			self._x = 1
		if self._secondPlayer == True:
			if self._y != 0:
				self.fullTurn()
			else:
				self._displayMessage("Waiting for Second Player.")
				return
		else:
			self.fullTurn()
			
	def inputPlay1Move4(self):
		if self._x == 0:
			self._play1Move = self._play1s[3]
			self._x = 1
		if self._secondPlayer == True:
			if self._y != 0:
				self.fullTurn()
			else:
				self._displayMessage("Waiting for Second Player.")
				return
		else:
			self.fullTurn()
	
	def inputPlay1Move5(self):
		if self._x == 0:
			self._play1Move = self._play1s[4]
			self._x = 1
		if self._secondPlayer == True:
			if self._y != 0:
				self.fullTurn()
			else:
				self._displayMessage("Waiting for Second Player.")
				return
		else:
			self.fullTurn()
				
	def inputPlay1Move6(self):
		if self._x == 0:
			self._play1Move = self._play1s[5]
			self._x = 1
		if self._secondPlayer == True:
			if self._y != 0:
				self.fullTurn()
			else:
				self._displayMessage("Waiting for Second Player.")
				return
		else:
			self.fullTurn()
	
	def inputPlay2Move1(self):
		if self._y == 0:
			self._play2Move = self._play2s[0]
			self._y = 1
		if self._x != 0:
			self.fullTurn()
		else:
			self._displayMessage("Waiting for First Player.")
			return
			
	def inputPlay2Move2(self):
		if self._y == 0:
			self._play2Move = self._play2s[1]
			self._y = 1
		if self._x != 0:
			self.fullTurn()
		else:
			self._displayMessage("Waiting for First Player.")
			return
				
	def inputPlay2Move3(self):
		if self._y == 0:
			self._play2Move = self._play2s[2]
			self._y = 1
		if self._x != 0:
			self.fullTurn()
		else:
			self._displayMessage("Waiting for First Player.")
			return
			
	def inputPlay2Move4(self):
		if self._y == 0:
			self._play2Move = self._play2s[3]
			self._y = 1
		if self._x != 0:
			self.fullTurn()
		else:
			self._displayMessage("Waiting for First Player.")
			return
	
	def inputPlay2Move5(self):
		if self._y == 0:
			self._play2Move = self._play2s[4]
			self._y = 1
		if self._x != 0:
			self.fullTurn()
		else:
			self._displayMessage("Waiting for First Player.")
			return
				
	def inputPlay2Move6(self):
		if self._y == 0:
			self._play2Move = self._play2s[5]
			self._y = 1
		if self._x != 0:
			self.fullTurn()
		else:
			self._displayMessage("Waiting for First Player.")
			return
			
	def endOfTurnAblities(self, player, NPC):
		if player.getPin() == "01001011":
				r = random.randint(1,100)
				p = 75
				a = (player.getMAXHP()/2)
				if player.getHP() <= a:
					p = 50
				if r >= p:
					player.setBuff(4)
					player.buffFighter()
					self._displayMessage("Thanks to Kanade's ability, Kanade's Dex was boosted")
					self._displayMessage("-----------------------------")
		if player.getPin() == "01000100":
				r = random.randint(1,100)
				p = 50
				if r >= p:
					for count in range(5):
						player.setBuff(2)
						player.buffFighter()
					self._displayMessage("Thanks to Seigfried's ability, Seigfried's Def was boosted")
					self._displayMessage("-----------------------------")
		if player.getPin() == "01010111":
			for count in range(3):
				r = random.randint(1,5)
				if r == 1:
					player.setBuff(1)
					player.buffFighter()
					self._displayMessage("Thanks to Alices ability, her Atk was Boosted.")
				elif r == 2:
					player.setBuff(3)
					player.buffFighter()
					self._displayMessage("Thanks to Alices ability, her Def was Boosted.")
				elif r == 3:
					player.setBuff(3)
					player.buffFighter()
					self._displayMessage("Thanks to Alices ability, her Acc was Boosted.")
				elif r == 4:
					player.setBuff(3)
					player.buffFighter()
					self._displayMessage("Thanks to Alices ability, her Dex was Boosted.")
			self._displayMessage("-----------------------------")
		if player.getPin() == "01010110":
			if player.getHP() != 0:
				a = (player.getMAXHP()/3)
				if player.getHP() < a:
					player.heal(player.getMAXHP()/10)
					self._displayMessage("Thanks to Rupert's ability, Rupert was healed for " + str(int(player.getMAXHP()/10)) + " points.")
					self._displayMessage("-----------------------------")
		if player.getPin() == "01000110":
			if self._omega == 0:
				NPC.setStatus(random.randint(1,5))
				t = " "
				if NPC.getStatus() == 1:
					t = " was burned"
				elif NPC.getStatus() == 2:
					t = " fell asleep"
				elif NPC.getStatus() == 3:
					t = " was paralyzed"
				elif NPC.getStatus() == 4:
					t = " was poisoned"
				elif NPC.getStatus() == 5:
					t = " was frozen"
				self._displayMessage("Thanks to Daiyousei's ability, " + NPC.getName() + t)
				self._displayMessage("-----------------------------")
				self._omega += 3
			else:
				self._omega -= 1
		if NPC.getPin() == "01001011":
				r = random.randint(1,100)
				p = 75
				a = (NPC.getMAXHP()/2)
				if NPC.getHP() <= a:
					p = 50
				if r >= p:
					NPC.setBuff(4)
					NPC.buffFighter()
					self._displayMessage("Thanks to Kanade's ability, Kanade's Dex was boosted")
					self._displayMessage("-----------------------------")
		if NPC.getPin() == "01000100":
				r = random.randint(1,100)
				p = 40
				if r >= p:
					for count in range(5):
						NPC.setBuff(2)
						NPC.buffFighter()
					self._displayMessage("Thanks to Seigfried's ability, Seigfried's Def was boosted")
					self._displayMessage("-----------------------------")
		if NPC.getPin() == "01010111":
			for count in range(3):
				r = random.randint(1,5)
				if r == 1:
					NPC.setBuff(1)
					NPC.buffFighter()
					self._displayMessage("Thanks to Alices ability, her Atk was Boosted.")
				elif r == 2:
					NPC.setBuff(3)
					NPC.buffFighter()
					self._displayMessage("Thanks to Alices ability, her Def was Boosted.")
				elif r == 3:
					NPC.setBuff(3)
					NPC.buffFighter()
					self._displayMessage("Thanks to Alices ability, her Acc was Boosted.")
				elif r == 4:
					NPC.setBuff(3)
					NPC.buffFighter()
					self._displayMessage("Thanks to Alices ability, her Dex was Boosted.")
			self._displayMessage("-----------------------------")
		if NPC.getPin() == "01010110":
			if NPC.getHP() != 0:
				a = (NPC.getMAXHP()/3)
				if NPC.getHP() < a:
					NPC.heal(int(NPC.getMAXHP()/10))
					self._displayMessage("Thanks to Rupert's ability, Rupert was healed for " + str(int(NPC.getMAXHP()/10)) + " points.")
					self._displayMessage("-----------------------------")
		if NPC.getPin() == "01000110":
			if self._sigma == 0:
				player.setStatus(random.randint(1,5))
				if player.getStatus() == 1:
					t = " was burned"
				elif player.getStatus() == 2:
					t = " fell asleep"
				elif player.getStatus() == 3:
					t = " was paralyzed"
				elif player.getStatus() == 4:
					t = " was poisoned"
				elif player.getStatus() == 5:
					t = " was frozen"
				self._displayMessage("Thanks to Daiyousei's ability, " + player.getName() + t)	
				self._displayMessage("-----------------------------")
				self._sigma += 3
			else:
				self._sigma -= 1
		return

	def fullTurn(self):
		if self._secondPlayer == True:
			if self.turnCalc(self._player1.getAgi(), self._player2.getAgi()):
				self.playerTurn(self._player1, self._player2, self._play1Move)
				if self._player1.getHP() <= 0 or self._player2.getHP() <=0:
					self.endBattle()
				else:
					self.updateAll()
				self.playerTurn(self._player2, self._player1, self._play2Move)
			else:
				self.playerTurn(self._player2, self._player1, self._play2Move)
				if self._player1.getHP() <= 0 or self._player2.getHP() <=0:
					self.endBattle()
				else:
					self.updateAll()
				self.playerTurn(self._player1, self._player2, self._play1Move)
		else:
			if self.turnCalc(self._player1.getAgi(), self._player2.getAgi()):
				self.playerTurn(self._player1, self._player2, self._play1Move)
				if self._player1.getHP() <= 0 or self._player2.getHP() <=0:
					self.endBattle()
					return
				else:
					self.updateAll()
				self.NPCEnemyTurn(self._player1, self._player2)
			else:
				self.NPCEnemyTurn(self._player1, self._player2)
				if self._player1.getHP() <= 0 or self._player2.getHP() <=0:
					self.endBattle()
					return
				else:
					self.updateAll()
				self.playerTurn(self._player1, self._player2, self._play1Move)
		self.endOfTurnAblities(self._player1, self._player2)
		if self._player1.getHP() <= 0 or self._player2.getHP() <=0:
			self.endBattle()
		else:
			self.updateAll()
			
	def updateAll(self):
		self._playerFrame.destroy()
		self._NPCFrame.destroy()
		if self._secondPlayer == True:
			t = "Player 1"
		else: 
			t = "Player"
		self._playerFrame = LabelFrame(self, text = t, padx = 5, pady = 5)
		self._playerFrame.grid(row = 0, column = 0, sticky = N+W)
		self._playerName = Label(self._playerFrame, text = self._player1.getName())
		self._playerName.grid(row = 0, sticky = W)
		self._playerHP = Label(self._playerFrame, text = (str(self._player1.getHP()) + "/" +str(self._player1.getMAXHP())))	
		self._playerHP.grid(row = 1, sticky = W)
		if self._player1.getStatus() == 1:
			t = "Burned"
		elif self._player1.getStatus() == 2:
			t = "Asleep"
		elif self._player1.getStatus() == 3:
			t = "Paralyzed"
		elif self._player1.getStatus() == 4:
			t = "Poisoned"
		elif self._player1.getStatus() == 5:
			t = "Frozen"
		else:
			t = "None"
		self._playerStatus = Label(self._playerFrame, text = ("Status: " + t))
		self._playerStatus.grid(row = 2, sticky = W)
		
		#Non-Player Character or opponent
		if self._secondPlayer == True:
			t = "Player 2"
		else: 
			t = "Opponent"
		self._NPCFrame = LabelFrame(self, text = t, padx = 5 , pady = 5)
		self._NPCFrame.grid(row = 0, column = 2, sticky = N+E)
		self._NPCName = Label(self._NPCFrame, text = self._player2.getName())
		self._NPCName.grid(row = 0 , sticky = W)
		self._NPCHP = Label(self._NPCFrame, text = (str(self._player2.getHP()) +"/" + str(self._player2.getMAXHP())))	
		self._NPCHP.grid(row = 1, sticky = W)
		if self._player2.getStatus() == 1:
			t = "Burned"
		elif self._player2.getStatus() == 2:
			t = "Asleep"
		elif self._player2.getStatus() == 3:
			t = "Paralyzed"
		elif self._player2.getStatus() == 4:
			t = "Poisoned"
		elif self._player2.getStatus() == 5:
			t = "Frozen"
		else:
			t = "None"
		self._NPCStatus = Label(self._NPCFrame, text = ("Status: " + t))
		self._NPCStatus.grid(row = 2, sticky = W)
		self._x = 0
		self._y = 0
		return
	
	def endBattle(self):
		if self._player1.getHP() <= 0:
			
			if self._secondPlayer == True:
				self.updateAll()
				self.after(500)
				tkinter.messagebox.showinfo(title = "Mystic Tourney", message = "Player 2 wins!")
				self.destroy()
				mainMenu()
			else:
				self.updateAll()
				self.after(500)
				tkinter.messagebox.showinfo(title = "Mystic Tourney", message = "You Lost.")
				self.destroy()
				mainMenu()
		else:
			if self._secondPlayer == True:
				self.updateAll()
				self.after(500)
				tkinter.messagebox.showinfo(title = "Mystic Tourney", message = "Player 1 wins!")
				self.destroy()
				mainMenu()
			else:
				self.updateAll()
				self.after(500)
				tkinter.messagebox.showinfo(title = "Mystic Tourney", message = "You Win!")
				self.destroy()
				mainMenu()
	
	def playerTurn(self, player, NPC, m):
		playerStatus = player.getStatus()
		if playerStatus == 2 or playerStatus == 3 or playerStatus == 5:
			r = random.randint(1,100)
			if playerStatus == 3:
				if r <= 50:
					self._displayMessage(player.getName() + " is paralyzed and cannot move")
					player.setTurn(player.getTurn() - 1)
					self._displayMessage("-----------------------------")
					return
			elif playerStatus == 2: 
				p = player.getPercent()
				if r <= p:
					self._displayMessage(player.getName() + " is asleep")
					player.setPercent(p-10)
					self._displayMessage("-----------------------------")
					return
				else:
					self._displayMessage(player.getName() + " woke up")
					player.setStatus(0)
			elif playerStatus == 5:	
				p = player.getPercent()
				if r <= p:
					self._displayMessage(player.getName() + " is frozen")
					player.setPercent(p-20)
					self._displayMessage("-----------------------------")
					return
				else:
					self._displayMessage(player.getName() + " thawed out")
					player.setStatus(0)
		self._displayMessage(player.getName() + " used " + m.getName())
		se = m.getSE()
		if se == 16:
			h = player.getMAXHP()/6
			self._displayMessage(player.getName() + " used " + m.getName())
			player.heal(int(h))
			self._displayMessage(player.getName() + " healed themself for " + str(int(h)) + " points")
		elif se > 0 and se < 6 and m.getStrength() == 0:
			if se == 1:
				NPC.setStatus(1)
				self._displayMessage(NPC.getName() + " was burned")
			elif se == 2:
				NPC.setStatus(2)
				self._displayMessage(NPC.getName() + " fell asleep")
			elif se == 3:
				NPC.setStatus(3)
				self._displayMessage(NPC.getName() + " was paralyzed")
			elif se == 4:
				NPC.setStatus(4)
				self._displayMessage(NPC.getName() + " was posioned")
			elif se == 5:
				NPC.setStatus(5)
				self._displayMessage(NPC.getName() + " was frozen")
		elif se > 10 and se < 16 or se == 19 and m.getStrength() == 0:
			if se == 19:
				se = random.randint(11,15)
			if se == 11:
				player.setBuff(1)
				self._displayMessage(player.getName() + " boosted their Atk")
			elif se == 12:
				player.setBuff(2)
				self._displayMessage(player.getName() + " boosted their Def")
			elif se == 13:
				player.setBuff(3)
				self._displayMessage(player.getName() + " boosted their Acc")
			elif se == 14:
				player.setBuff(4)
				self._displayMessage(player.getName() + " boosted their Dex")
			elif se == 15:
				player.setBuff(5)
				self._displayMessage(player.getName() + " boosted their Agi")
		elif self.atkHitCalc(player.getAcc(), NPC.getDex()) == True:
			s = m.getStrength()
			NPCstatus = NPC.getStatus()
			if se - 5 == NPCstatus:
				s = s*2
			if player.getPin() == "01010101":
				r = random.randint(1,100)
				p = 60
				if r >= p:
					a = 1
					d = self.damageCalculation(player.getAtk(), a, s)
					self._displayMessage("Thanks to Lena's ability, she ignored " + NPC.getName() + "'s Def")
					self._displayMessage("-----------------------------")
				else:			
					d = self.damageCalculation(player.getAtk(), NPC.getDefense(), s)
			else:			
				d = self.damageCalculation(player.getAtk(), NPC.getDefense(), s)
			d = int(d)
			self._displayMessage(player.getName() + " did " + str(d) + " points of damage to " + NPC.getName())
			NPC.takeDamage(d)
			if se == 17:
				self._displayMessage(player.getName() + " healed themself for " + str(d) + " points")
				player.heal(d)
			elif se > 0 and se < 6 or se == 18:
				r = random.randint(1,100)
				if se == 18:
					se = random.randint(1,5)
					if se == 1:
						NPC.setStatus(1)
						self._displayMessage(NPC.getName() + " was burned")
					elif se == 2:
						NPC.setStatus(2)
						self._displayMessage(NPC.getName() + " fell asleep")
					elif se == 3:
						NPC.setStatus(3)
						self._displayMessage(NPC.getName() + " was paralyzed")
					elif se == 4:
						NPC.setStatus(4)
						self._displayMessage(NPC.getName() + " was posioned")
					elif se == 5:
						NPC.setStatus(5)
						self._displayMessage(NPC.getName() + " was frozen")
				elif se == 1:
					if r > 60:
						NPC.setStatus(1)
						self._displayMessage(NPC.getName() + " was burned")
				elif se == 2:
					if r > 60:
						NPC.setStatus(2)
						self._displayMessage(NPC.getName() + " fell asleep")
				elif se == 3:
					if r > 60:
						NPC.setStatus(3)
						self._displayMessage(NPC.getName() + " was paralyzed")
				elif se == 4:
					if r > 80:
						NPC.setStatus(4)
						self._displayMessage(NPC.getName() + " was posioned")
				elif se == 5:
					if r > 80:
						NPC.setStatus(5)
						self._displayMessage(NPC.getName() + " was frozen")
			elif se > 10 and se < 16 or se == 19:
				if se == 19:
					se = random.randint(11,15)
				if se == 11:
					player.setBuff(1)
					self._displayMessage(player.getName() + " boosted their Atk")
				elif se == 12:
					player.setBuff(2)
					self._displayMessage(player.getName() + " boosted their Def")
				elif se == 13:
					player.setBuff(3)
					self._displayMessage(player.getName() + " boosted their Acc")
				elif se == 14:
					player.setBuff(4)
					self._displayMessage(player.getName() + " boosted their Dex")
				elif se == 15:
					player.setBuff(5)
					self._displayMessage(player.getName() + " boosted their Agi")
		else:
			self._displayMessage(player.getName() + "'s Attack Missed.")
		self._displayMessage("-----------------------------")
		player.buffFighter()
		if playerStatus == 1 or playerStatus == 3 or playerStatus == 4:
			if player.getTurn() != 0:
				player.setTurn(player.getTurn() - 1)
				if playerStatus == 1:
					player.takeDamage(int(player.getMAXHP()/10))
					self._displayMessage(player.getName() + " took " + str(int(player.getMAXHP()/10)) + " points of burn damage.")
				if playerStatus == 4:
					player.takeDamage(int(player.getMAXHP()/8))
					self._displayMessage(player.getName() + " took " + str(int(player.getMAXHP()/8)) + " points of posion damage.")
			else:
				if playerStatus == 1:
					self._displayMessage(player.getName() + " recovered from the burn")
					player.setStatus(0)
				if playerStatus == 3:
					self._displayMessage(player.getName() + " recovered from the paralysis")
					player.setStatus(0)	
				if playerStatus == 4:
					self._displayMessage(player.getName() + " recovered from the posion")
					player.setStatus(0)
			self._displayMessage("-----------------------------")	
		return
	
	def NPCEnemyTurn(self, player, NPC):
		"""The Enemy turn"""
		movefile = NPC.getPin() + ".txt"
		movefile = movefile.strip()
		NPCMoveSet = Set(movefile)
		NPCstatus = NPC.getStatus()
		if NPCstatus == 2 or NPCstatus == 3 or NPCstatus == 5:
			r = random.randint(1,100)
			if NPCstatus == 3:
				if r <= 50:
					self._displayMessage(NPC.getName() + " is paralyzed and cannot move")
					NPC.setTurn(NPC.getTurn() - 1)
					self._displayMessage("-----------------------------")
					return
			elif NPCstatus == 2: 
				p = NPC.getPercent()
				if r <= p:
					self._displayMessage(NPC.getName() + " is asleep")
					NPC.setPercent(p-10)
					self._displayMessage("-----------------------------")
					return
				else:
					self._displayMessage(str(NPC.getName() + " woke up"))
					NPC.setStatus(0)
			elif NPCstatus == 5:	
				p = NPC.getPercent()
				if r <= p:
					self._displayMessage(NPC.getName() + " is frozen")
					NPC.setPercent(p-20)
					self._displayMessage("-----------------------------")
					return
				else:
					self._displayMessage(NPC.getName() + " thawed out")
					NPC.setStatus(0)
		a = (NPC.getMAXHP()/2)
		if NPC.getHP() <= a:
			templist = []
			for count in range(len(NPCMoveSet._moveSet)-1):
				m = NPCMoveSet._moveSet[count]
				se = m.getSE()
				if se == 16 or se == 17 or se == 12 or se == 14:
					templist.append(m)
				templist.append(m)
			r = random.randint(0,(len(templist) - 1))
			m = templist[r]
		else:
			r = random.randint(0,5)
			m = NPCMoveSet.getMove(r)
		self._displayMessage(NPC.getName() + " used " + m.getName())
		se = m.getSE()
		if se == 16:
			h = NPC.getMAXHP()/6
			self._displayMessage(NPC.getName() + " used " + m.getName())
			NPC.heal(int(h))
			self._displayMessage(NPC.getName() + " healed themself for " + str(int(h)) + " points")
		elif (se > 0 and se < 6 or se == 18) and m.getStrength() == 0:
			if se == 18:
				se = random.randint(1,5)
			if se == 1:
				player.setStatus(1)
				self._displayMessage(player.getName() + " was burned")
			elif se == 2:
				player.setStatus(2)
				self._displayMessage(player.getName() + " fell asleep")
			elif se == 3:
				player.setStatus(3)
				self._displayMessage(player.getName() + " was paralyzed")
			elif se == 4:
				player.setStatus(4)
				self._displayMessage(player.getName() + " was posioned")
			elif se == 5:
				player.setStatus(5)
				self._displayMessage(player.getName() + " was frozen")
		elif (se > 10 and se < 16 or se == 19) and m.getStrength() == 0:
			if se == 19:
				se = random.randint(11,15)
			if se == 11:
				NPC.setBuff(1)
				self._displayMessage(NPC.getName() + " boosted their Atk")
			elif se == 12:
				NPC.setBuff(2)
				self._displayMessage(NPC.getName() + " boosted their Def")
			elif se == 13:
				NPC.setBuff(3)
				self._displayMessage(NPC.getName() + " boosted their Acc")
			elif se == 14:
				NPC.setBuff(4)
				self._displayMessage(NPC.getName() + " boosted their Dex")
			elif se == 15:
				NPC.setBuff(5)
				self._displayMessage(NPC.getName() + " boosted their Agi")
		elif self.atkHitCalc(NPC.getAcc(), player.getDex()) == True:
			s = m.getStrength()
			playerStatus = player.getStatus()
			if se - 5 == playerStatus:
				s = s*2
			if NPC.getPin() == "01010101":
					r = random.randint(1,100)
					p = 50
					if r >= p:
						a = 1
						d = self.damageCalculation(NPC.getAtk, a, s)
						self._displayMessage("Thanks to Lena's ability, she ignored " + player.getName() + "'s Def")
						self._displayMessage("-----------------------------")
					else:			
						d = self.damageCalculation(NPC.getAtk(), player.getDefense(), s)
			else:			
				d = self.damageCalculation(NPC.getAtk(), player.getDefense(), s)
			d = int(d)
			self._displayMessage(NPC.getName() + " did " + str(d) + " points of damage to " + player.getName())
			player.takeDamage(d)
			if se == 17:
				self._displayMessage(NPC.getName() + " healed themself for " + str(d) + " points")
				NPC.heal(d)
			elif se > 0 and se < 6 or se == 18:
				r = random.randint(1,100)
				if se == 18:
					se = random.randint(1,5)
					if se == 1:
						player.setStatus(1)
						self._displayMessage(player.getName() + " was burned")
					elif se == 2:
						player.setStatus(2)
						self._displayMessage(player.getName() + " fell asleep")
					elif se == 3:
						player.setStatus(3)
						self._displayMessage(player.getName() + " was paralyzed")
					elif se == 4:
						player.setStatus(4)
						self._displayMessage(player.getName() + " was posioned")
					elif se == 5:
						player.setStatus(5)
						self._displayMessage(player.getName() + " was frozen")
				elif se == 1:
					if r > 60:
						player.setStatus(1)
						self._displayMessage(player.getName() + " was burned")
				elif se == 2:
					if r > 60:
						player.setStatus(2)
						self._displayMessage(player.getName() + " fell asleep")
				elif se == 3:
					if r > 60:
						player.setStatus(3)
						self._displayMessage(player.getName() + " was paralyzed")
				elif se == 4:
					if r > 80:
						player.setStatus(4)
						self._displayMessage(player.getName() + " was posioned")
				elif se == 5:
					if r > 80:
						player.setStatus(5)
						self._displayMessage(player.getName() + " was frozen")
			elif se > 10 and se < 16 or se == 19:
				if se == 19:
					se = random.randint(11,15)
				if se == 11:
					NPC.setBuff(1)
					self._displayMessage(NPC.getName() + " boosted their Atk")
				elif se == 12:
					NPC.setBuff(2)
					self._displayMessage(NPC.getName() + " boosted their Def")
				elif se == 13:
					NPC.setBuff(3)
					self._displayMessage(NPC.getName() + " boosted their Acc")
				elif se == 14:
					NPC.setBuff(4)
					self._displayMessage(NPC.getName() + " boosted their Dex")
				elif se == 15:
					NPC.setBuff(5)
					self._displayMessage(NPC.getName() + " boosted their Agi")
			
		else:
			self._displayMessage(NPC.getName() + "'s Attack Missed.")
		self._displayMessage("-----------------------------")
		NPC.buffFighter()
		if NPCstatus == 1 or NPCstatus == 3 or NPCstatus == 4:
			if NPC.getTurn() != 0:
				NPC.setTurn(player.getTurn() - 1)
				if NPCstatus == 1:
					NPC.takeDamage(int(NPC.getMAXHP()/10))
					self._displayMessage(NPC.getName() + " took " + str(int(NPC.getMAXHP()/10)) + " points of burn damage.")
				if NPCstatus == 4:
					NPC.takeDamage(int(NPC.getMAXHP()/8))
					self._displayMessage(NPC.getName() + " took " + str(int(NPC.getMAXHP()/8)) + " points of posion damage.")
			else:
				if NPCstatus == 1:
					self._displayMessage(player.getName() + " recovered from the burn")
					player.setStatus(0)
				if NPCstatus == 3:
					self._displayMessage(player.getName() + " recovered from the paralysis")
					player.setStatus(0)	
				if NPCstatus == 4:
					self._displayMessage(player.getName() + " recovered from the posion")
					player.setStatus(0)
		self._displayMessage("-----------------------------")
		return
def main():
	mainMenu().mainloop()
main()