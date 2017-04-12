class Dojo(object):
	"""docstring for Dojo"""
	def __init__(self):
		self.dojo_name=""


class Room(Dojo):
	"""docstring"""

	def __init__(self,name,room_type):
		Dojo.__init__(self)
		self.list_of_occupants=[]
		self.name=name
		self.room_type=room_type

	

class Office(Room):
	"""Class Office inherits Room"""
	def __init__(self,name,room_type):
		Room.__init__(self,name,room_type)
		self.max_occupants=6

	
class LivingSpace(Room):
	"""docstring for LivingSpace"""
	def __init__(self,name,room_type):
		Room.__init__(self,name,room_type)
		self.max_occupants=4


class Person():
	def __init__(self,firstname,secondname,person_type):
		self.firstname=firstname
		self.secondname=secondname
		self.persons=person_type
		self.office_name=""

	
class Fellow(Person):
	def __init__(self,firstname,secondname,person_type):
		self.person_type="Fellow"
		Person.__init__(self,firstname,secondname,self.person_type)
		self.livingspaceNumber=""
		
	
class Staff(Person):
	def __init__(self,firstname,secondname,person_type):
		self.person_type="staff"
		Person.__init__(self,firstname,secondname,self.person_type)

	

