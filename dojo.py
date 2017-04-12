class Dojo(object):
	"""docstring for Dojo"""
	def __init__(self):
		self.dojo_name=""


class Room(Dojo):
	"""docstring"""

	def __init__(self,room_name,room_type):
		Dojo.__init__(self)
		self.list_of_occupants=[]
		self.room_name=room_name
		self.room_type=room_type

	

class Office(Room):
	"""Class Office inherits Room"""
	def __init__(self,room_name,room_type):
		Room.__init__(self,room_name,room_type)
		self.max_occupants=6

	
class LivingSpace(Room):
	"""docstring for LivingSpace"""
	def __init__(self,room_name,room_type):
		Room.__init__(self,room_name,room_type)
		self.max_occupants=4
