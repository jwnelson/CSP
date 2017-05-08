import sys, os
import importlib

class ASCOS:
	"""
		Autonomous Spacecraft Operating System

		The main operating system for the spacecraft that the player interfaces with.
		Parses user input line by line for commands and runs the specified programs.
	"""

	def __init__(self, player, spacecraft, gameinfo):
		self.player = player
		self.spacecraft = spacecraft
		self.gameinfo = gameinfo

		self.programs = self._generate_program_dict() # get a dict of all available programs

	def _generate_program_dist(self):
		"""
			Automatically generate a list of programs from modules in programs/
		"""
		programs = {}
		for program in os.listdir("programs"):
			if program != "program.py" and program != "__init__.py":
				programs.append(program.rstrip(".py"))

		return programs



	def handle_input(self, rawinput):
		"""
			Handles player input to the terminal.
		"""
		input_ = rawinput.split('')
		program = None
		options = None

		# parse the command and options from the input
		if input_[0] in self.commands:
			program = self.programs[input_]
			if len(input_) > 1:
				options = input_[1:]
			else:
				options = []

			# run the program with the given options list 
			result = program.run(options)
		else:


			

