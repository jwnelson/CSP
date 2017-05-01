class Object:
	"""
		Generic planetary/stellar object. All stars, planets, comets, and asteroids
		subclass this class.
	"""

	def __init__(self, mass, collision_radius, position):

class Planet(Object):
	"""
		A generic planet class. Individual planet types sublcass this.
	"""
	def __init__(self, )

class Moon(Object):

	def __init__(self):
		Object.__init__(self)
class Star(Object):
	"""
		A generic star class.
	"""

class Asteroid(Object):

class Comet(Object):