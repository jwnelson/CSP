import threading

class GameManager:
	"""
		Primary game management class.

		GameManager manages game threads and players.
		There should be only ONE GameEngine instance
	"""

	def __init__(self):
		# Setup the network

	def new_game(self,):
		pass

	def create_player(self, ):

	def run
		"""
			Main loop
		"""
		

class GameThread(threading.Thread):
	"""
		The main game thread class.

		Each active game is spawned off as its own thread.
		Handles player commands, output to player, and manages all game events.
	"""

	def __init__(self, player):
		threading.Thread.__init__(self)
		self.player = player

		self.init_game()

	def init_game(self):
		"""
			Initializes a new game.
		"""
		pass

	def run_game(self):


