import random

from dojo import Room,Office,LivingSpace
from people import Person,Fellow,Staff


"""
Implementations of functionalities

Create rooms
"""


class Implementation():
	all_rooms=[]#variable to hold all rooms in a dojo
	all_people=[]#variable to hold all people  in a dojo
	available_offices=[]#variable to hold offices with space to be allocated

	def create_room(self,room_name,room_type):
		#check whether room_name is in the list of existing rooms in dojo
		if room_name in [room_object.room_name for room_object in self.all_rooms]:
			print("{} is already taken, try a different one".format(room_name))
			return False

		#if it does not exist,create the room
		else:
			if room_type.lower()=="office":
				room_object=Office(room_name,room_type.lower())
				self.all_rooms.append(room_object)
				print ("An office called {} has been successfully created!".format(room_name))
				return room_object

			elif room_type.lower()=="livingspace":
				room_object=LivingSpace(room_name,room_type.lower())
				"""
				Be careful not to save the name of an office;rather save the object since you can get its attributes
				NB:name is a string """
				self.all_rooms.append(room_object)
				print ("A Living Space called {} has been successfully created!".format(room_name))
				return room_object
			else:
				return ("Not a valid room")
		print(existing_rooms)

	def allocate_office(self,person_object):
		"""
		This function takes as an argument an object of type person,whose attribute 
		office_name is set according to one of the available office Space
		Logic:
		    loop through a list with objects of type office checking the first with 
		    available space,add to its list_of_occupants attribute the name of the 
		    person object received as argument

		return:
		    dictionary object for the purpose of testcases  
		"""
		available_rooms=self.all_rooms
		##create a list of objects whose type is office and have an empty space
		available_offices=[room_object for room_object in available_rooms if room_object.room_type=='office' and len(room_object.list_of_occupants)<6]
		

		##randomize the list first and get the last object in it
		##NB:You can decide on whether to get the last or the first object
		random.shuffle(available_offices)
		if len(available_offices)!=0:
			office_to_allocate=available_offices.pop()

			#Now assign the person this office
			office_to_allocate.list_of_occupants.append(person_object)
			#set the attribute office_name of object person to the name of the asigned office
			person_object.office_name=office_to_allocate.room_name

			print("{} {} has been allocated the office {}".format(person_object.firstname,person_object.secondname,office_to_allocate.room_name))
			allocations={"office":office_to_allocate.room_name}
			return allocations
		else:
			print("{} {} has not been allocated any office!".format(self.person.firstname,person_object.secondname))
			return {'office':None}
			


	def allocate_livingspace(self,person_object):
		"""
		This function takes as an argument an object of type person,whose attribute 
		livingspacename is set according to one of the available livingspaces
		Logic:
		    loop through a list with objects of type office checking the first with 
		    available space,add to its list_of_occupants attribute the name of the 
		    person object received as argument

		return:
		    office_name or None  
		"""
		#Let's check whether the person can be allocated livingspace
		if person_object.person_type.lower()!='staff':
			available_rooms=self.all_rooms
			##create a list of objects whose type is office and have an empty space
			available_living_spaces=[room_object for room_object in available_rooms if room_object.room_type=='livingspace' and len(room_object.list_of_occupants)<4]

			##randomize the list first and get the last object in it
			##NB:You can decide on whether to get the last or the first object
			random.shuffle(available_living_spaces)

			if len(available_living_spaces)!=0:
				livingspace=available_living_spaces.pop()
				#Now assign the person this office
				livingspace.list_of_occupants.append(person_object)
				#set the attribute office_name of object person to the name of the asigned office
				person_object.livingspace=livingspace.room_name
				print("{} {} has been allocated the livingspace {}".format(self.person.firstname,self.person.secondname,livingspace.room_name))
				return livingspace.room_name
			else:
				print("{} {} has not been allocated any livingspace!".format(self.person.firstname,self.person.secondname))
				return None
			


	def add_person(self,firstname,secondname,person_type,wants_accommodation="N"):
		
		if person_type.lower()=="fellow":
			self.person=Fellow(firstname,secondname,person_type)
			self.all_people.append(self.person)

			print("{} {} has been successfully added.".format(self.person.firstname,self.person.firstname))
			self.allocate_office(self.person)
			##Allocate livingspace if fellow and chose livingspace option Y
			if wants_accommodation=='y' or wants_accommodation=='Y':
				self.allocate_livingspace(self.person)

			return self.person

		elif person_type.lower()=="staff":
			self.person=Staff(firstname,secondname,person_type)
			self.all_people.append(self.person)
			self.allocate_office(self.person)
			return self.person

		else:
			return "Not valid person"

	def print_room(self,room_name):
		"""
		This function prints each room together with names of its occupants

		"""
		##single out the particular room from self.all_rooms
		self.room_to_list_its_occupants=[room_object for room_object in self.all_rooms if room_object.room_name==room_name]
		size=len(self.room_to_list_its_occupants[0].list_of_occupants)
		names_of_occupants=[]
		for index in range(0,size):
			#print(self.temp_room[0].list_of_occupants[index].firstname,self.temp_room[0].list_of_occupants[index].secondname)
			names_of_occupants.extend(['{} {}'.format(self.room_to_list_its_occupants[0].list_of_occupants[index].firstname,self.room_to_list_its_occupants[0].list_of_occupants[index].secondname)])

		print(names_of_occupants)
		return names_of_occupants

	def print_allocations(self,file=""):
		"""loop over the rooms list_of_occupants"""
		self.room_names=[]

		print(self.all_rooms)
		for index in range(0,len(self.all_rooms)):
			self.room_names.append(self.all_rooms[index].room_name)

		print(self.room_names)

		while len(self.room_names)!=0:
			for person_object in self.all_people:
				pass



