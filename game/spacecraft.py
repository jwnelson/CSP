class Subsystem:
	"""
		Generic subsystem parent class
	"""
	
	def status(self):
		"""
			Return status information about this subsystem
		"""
		pass

class Prop(Subsystem):
	"""
		Propulsion subsystem class
	"""
	pass

class Power(Subsystem):
	"""
		Electrical subsystem class.
	"""
	pass

class Thermal(Subsystem):
	"""
		Thermal subsystem class.
	"""
	pass

class Avionics(Subsystem):
	"""
		Avionics subsystem class.
	"""
	pass

class Actuators(Subsystem):
	"""
		Actuator subsystem class.
	"""
	pass

class Camera(Subsystem):
	pass

class ISRU(Subsystem):
	pass

class Instruments(Subsystem):
	pass

class Navigation(Subsystem):
	pass

class Spacecraft:
	"""
		Main spacecraft class
	"""

	def __init__(self, config):
		self.config = sc_config

		self.load_config()

	def load_config(self):
		"""
			Load spacecraft configuration info from a config file and
			initialize spacecraft attributes.
		"""
		self.Prop = None
		self.Power = None
		self.Thermal = None
		self.Avionics = None
		self.Actuators = None
		self.Camera = None
		self.ISRU = None
		self.Instruments = None
		self.Navigation = None

		self.subsystems = {
							"Prop": self.Prop,
							"Power": self.Power,
							"Thermal": self.Thermal,
							"Avionics": self.Avionics,
							"Actuators": self.Actuators,
							"Camera": self.Camera,
							"ISRU": self.ISRU,
							"Instruments": self.Instruments,
							"Navigation" : self.Navigation
		}
