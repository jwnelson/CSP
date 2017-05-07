
class Session:
	"""
		Class that handles an individual game session.
	"""

	def __init__(self, client_address):
		self.client_address = client_address

		self.client_authenticated = False

	def authenticate(self, user, password):
		"""
			Handles user login and authentication
		"""
		if user == "root" and password == "toor":
			return True
		else:
			return False

	def handle_input(self, input):
		"""
			Handles a single line of raw text input from a player.
		"""