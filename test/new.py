class Players():
	'''Player Class movement/animation !'''
	def __init__(self,health,energy):
		self.health = health
		self.energy = energy

	def player_energy(self):
		self.energy = 50

players = Players(20,10)
players.player_energy()
print(players.energy)

class Enemy():
	'''Player Class movement/animation !'''
	def __init__(self,health,energy):
		self.health = health
		self.energy = energy

	def enemy_energy(self):
		self.energy = 50

	def enemy_health(self):
		self.health = 100

enemys = Enemy(20,10)
enemys.player_energy()

print(enemys.energy)