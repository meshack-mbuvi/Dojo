class Dojo(object):
	"""docstring for Dojo"""
	def __init__(self):
		"""docstring"""
		pass
		

	def create_room(self,room_type,room_name):
		pass

class Room(Dojo):
	"""docstring"""

	def __init__(self):
		self.number_of_occupants=0
		self.all_rooms=[]

	def create_room(self,room_type,room_name):
		self.room_type=room_type
		self.room_name=room_name
		self.all_rooms.append(room_name)
		return self

	def allocate_room(self,room):
		"""This function checks whether an office can be allocated or not based on the current number of occupants.
		If on adding an extra member to the office exceeds the maximum allowable number of occupants, the office 
		allocation process is aborted
		"""
		if (self.number_of_occupants+1)<7:
			self.number_of_occupants+=1
			return"Office allocated successfully"
		else:
			return "Office has no extra space"

class Office(Room):
	"""Class Office inherits Room"""
	def __init__(self):
		self.max_occupands=6

	
class LivingSpace(Room):
	"""docstring for LivingSpace"""
	def __init__(self):
		super(Room,self).__init__()
		

	def allocate_room(self,room_name):
		if (self.number_of_occupants+1)<5:
			self.number_of_occupants+=1

class Person(Dojo):
	def __init__(self):
		self.name=""
		self.persons=[]

	def add_person(self,name,person_type):
		self.name=name
		self.person_type=person_type
		self.persons.append(name)
		return self

class Fellow(Person):
	def __init__(self):
		super(Person,self).__init__()
		self.person_type="Fellow"
		

class Staff(Person):
	def __init__(self):
		self.person_type="Staff"

