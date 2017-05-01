
class Player:
	"""
		An individual player. Stores, retrieves, and updates all information
		about a player's active game so that a player's game can continue between
		active sessions.
	"""

	def __init__(self, player_id, password, last_ip = None, use):
		self.player_id = None
		self.__password = None

		self.last_ip = None
		self.first_session = None
		self.last_session = None

		self.active_game = False
		self.longest_game = None
		self.games_played = 0

		self.current_game_duration = None
		self.game_time = None
		self.current_location = None

	def change_password(self, newpass):
		self.password = newpass
		return True

class PlayerDB:
	"""
		Creates, stores, and retrieves player instances.
	"""

