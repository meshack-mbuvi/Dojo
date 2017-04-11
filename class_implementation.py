from class_definitions import Office,LivingSpace,Fellow,Staff

"""
Implementations of functionalities

Create rooms
"""


class Implementation():
	all_rooms=[]
	all_people=[]
	available_offices=[]

	def create_room(self,name,room_type):

		if room_type.lower()=="office":
			room=Office(name,room_type.lower())
			Implementation.all_rooms.append(room.name)
			print ("An office called {} has been successfully created!".format(name))
			return room

		elif room_type.lower()=="livingspace":
			room=LivingSpace(name,room_type.lower())
			Implementation.all_rooms.append(room.name)
			print ("A Living Space called {} has been successfully created!".format(name))
			return room
		else:
			print ("Not a valid room")


	def add_person(self,name,person_type,acco="N"):
		
		if person_type.lower()=="fellow":
			self.person=Fellow(name,person_type)
			Implementation.all_people.append(self.person)
			return self.person

		elif person_type.lower()=="staff":
			self.person=Staff(name,person_type)
			Implementation.all_people.append(self.person)
			allocate_office(self.person.name)
			return person
		else:
			return "Not valid person"

		
