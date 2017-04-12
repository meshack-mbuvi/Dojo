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

		#create a list of names in existence so far
		existing_rooms=[]
		for index in range(0,len(self.all_rooms)):
			existing_rooms.append(self.all_rooms[index].name)
		if name in existing_rooms:
			print("Room name aleady taken")
			return False


		else:
			if room_type.lower()=="office":
				self.room=Office(name,room_type.lower())
				self.all_rooms.append(self.room)
				print ("An office called {} has been successfully created!".format(name))
				return self.room

			elif room_type.lower()=="livingspace":
				self.room=LivingSpace(name,room_type.lower())
				"""
				Be careful not to save the name of an office;rather save the object since you can get its attributes
				NB:name is a string """
				self.all_rooms.append(self.room)
				print ("A Living Space called {} has been successfully created!".format(name))
				return self.room
			else:
				return ("Not a valid room")

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
		rooms=self.all_rooms
		##create a list of objects whose type is office and have an empty space
		available_offices=[room for room in rooms if room.room_type=='office' and len(room.list_of_occupants)<6]
		

		##randomize the list first and get the last object in it
		##NB:You can decide on whether to get the last or the first object
		random.shuffle(available_offices)
		if len(available_offices)!=0:
			office=available_offices.pop()

			#Now assign the person this office
			office.list_of_occupants.append(person_object)
			#print rooms
			#set the attribute office_name of object person to the name of the asigned office
			person_object.office_name=office.name

			print("{} {} has been allocated the office {}".format(person_object.firstname,person_object.secondname,office.name))
			allocations={"office":office.name}
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
			rooms=self.all_rooms
			##create a list of objects whose type is office and have an empty space
			available_living_spaces=[room for room in rooms if room.room_type=='livingspace' and len(room.list_of_occupants)<4]

			##randomize the list first and get the last object in it
			##NB:You can decide on whether to get the last or the first object
			random.shuffle(available_living_spaces)

			if len(available_living_spaces)!=0:
				livingspace=available_living_spaces.pop()
				#Now assign the person this office
				livingspace.list_of_occupants.append(person_object)
				#set the attribute office_name of object person to the name of the asigned office
				person_object.livingspace=livingspace.name
				print("{} {} has been allocated the livingspace {}".format(self.person.firstname,self.person.secondname,livingspace.name))
				return livingspace.name
			else:
				print("{} {} has not been allocated any livingspace!".format(self.person.firstname,self.person.secondname))
				return None
			


	def add_person(self,firstname,secondname,person_type,acco="N"):
		
		if person_type.lower()=="fellow":
			self.person=Fellow(firstname,secondname,person_type)
			self.all_people.append(self.person)

			print("{} {} has been successfully added.".format(self.person.firstname,self.person.firstname))
			self.allocate_office(self.person)
			##Allocate livingspace if fellow and chose livingspace option Y
			if acco.lower()=='y':
				self.allocate_livingspace(self.person)

			return self.person

		elif person_type.lower()=="staff":
			self.person=Staff(firstname,secondname,person_type)
			self.all_people.append(self.person)
			self.allocate_office(self.person)
			return self.person

		else:
			return "Not valid person"

	def print_room(self,name):
		"""
		This function prints each room together with names of its occupants

		"""
		##single out the particular room from self.all_rooms
		self.temp_room=[room for room in self.all_rooms if room.name==name]
		size=len(self.temp_room[0].list_of_occupants)
		names=[]
		for index in range(0,size):
			#print(self.temp_room[0].list_of_occupants[index].firstname,self.temp_room[0].list_of_occupants[index].secondname)
			names.extend(['{} {}'.format(self.temp_room[0].list_of_occupants[index].firstname,self.temp_room[0].list_of_occupants[index].secondname)])


		print(names)
		return names

