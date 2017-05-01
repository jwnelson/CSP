class program:
	"""
		Base class for programs that run on the ASCOS
	"""

	def run(self):
		pass

	def interrupt(self):
		pass

	def quit(self):
		pass


class ASCOS:
	"""
		Autonomous SpaceCraft Operating System

		The main operating system for the spacecraft that the player interfaces with
	"""
	def __init__(self, programs):
		self.programs = programs # dict of available programs


	def cd(self, newdir):
		pass

	def ls(self):
		pass

	def help(self):
		pass

	def run_program(self, program):
		pass

