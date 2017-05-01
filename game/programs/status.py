import program

class Status(program.Program):
	"""
		Status program class.

		Displays status information about current spacecraft systems.
	"""

	def __init__(self, spacecraft, status_command = None):
		program.Program.__init__()

		self.subsystems = spacecraft.subsystems
		self.response = None


	
	def usage(self):
		pass

	def all_status(self):
		pass

	def run(self, status_command):
		"""
			Returns a status report from the selected subsystem,
			or a summarized report of all systems
		"""
		if status_command is None:
			return self.all_status()
		elif status_command in self.subsystems.keys():
			sub = self.subsystems[status_command]
			return sub.status()
		else:
			self.usage()
			return False
