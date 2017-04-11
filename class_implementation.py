import random

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
			self.all_rooms.append(room)
			print ("An office called {} has been successfully created!".format(name))
			return room

		elif room_type.lower()=="livingspace":
			room=LivingSpace(name,room_type.lower())
			"""
			Be careful not to save the name of an office;rather save the object since you can get its attributes
			NB:name is a string 
			"""
			self.all_rooms.append(room)
			print ("A Living Space called {} has been successfully created!".format(name))
			return room
		else:
			print ("Not a valid room")

	def allocate_office(self,person_object):
		"""
		This function takes as an argument an object of type person,whose attribute 
		office_name is set according to one of the available office Space
		Logic:
		    loop through a list with objects of type office checking the first with 
		    available space,add to its list_of_occupants attribute the name of the 
		    person object received as argument

		return:
		    office_name or None  
		"""
		rooms=self.all_rooms
		##create a list of objects whose type is office and have an empty space
		available_offices=[room for room in rooms if room.room_type=='office' and len(room.list_of_occupants)<6]

		##randomize the list first and get the last object in it
		##NB:You can decide on whether to get the last or the first object
		random.shuffle(available_offices)
		if len(available_offices)!=0:
			office=available_offices.pop()
			#Now assign the person this office
			office.list_of_occupants.append(person_object.name)
			#set the attribute office_name of object person to the name of the asigned office
			person_object.office_name=office.name
			return office.name
		else:
			return None



	def add_person(self,name,person_type,acco="N"):
		
		if person_type.lower()=="fellow":
			self.person=Fellow(name,person_type)
			self.all_people.append(self.person)

			print("{} has been successfully added.".format(self.person.name))
			office_allocated=self.allocate_office(self.person)

			#check whether office allocation has taken place
			if office_allocated!=None:
				print("{} has been allocated the office {}".format(self.person.name,office_allocated))

			else:
				print("{} has not been allocated any office!".format(self.person.name))
			return self.person

		elif person_type.lower()=="staff":
			self.person=Staff(name,person_type)
			self.all_people.append(self.person)
			allocate_office(self.person)
			return person

		else:
			return "Not valid person"

	

		
