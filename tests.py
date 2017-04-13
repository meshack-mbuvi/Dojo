import unittest
from implementation import Implementation


class TestCreateRoom(unittest.TestCase):
	"""This"""
	def setUp(self):
		self.implementation=Implementation()

	def test_create_room_successfully(self):
		room_object_created=self.implementation.create_room("Red","Livingspace")
		self.assertEqual(room_object_created.room_name,"Red",msg="Room names should match")

	def test_create_existing_room_fails(self):
		room_name_created=self.implementation.create_room("white","Livingspace")
		self.assertTrue(room_name_created,False)

	def test_not_allocate_office_not_existing(self):
		person=self.implementation.add_person("mutua","Mailu","Fellow")
		self.assertEqual(person.office_name,"",msg="should not allocate office that does not exist")

	def test_create_room_having_name_with_numbers_fails(self):
		new_person=self.implementation.create_room("mbuvi123242","office")
		self.assertEqual(new_person,"Not a valid room in our context")

class TestCheckPerson(unittest.TestCase):
	"""docstring for TestCheckRooms"""
	def setUp(self):
		self.implementation=Implementation()
		self.implementation.add_person("meshack","Mbuvi","Fellow")

	
	def test_add_person_succeeds(self):
		new_person=self.implementation.add_person("jacob","mutua","fellow")
		#create list with names of person object in the system
		names_people_in_system=[]
		for people in self.implementation.all_people:
			#create a single name
			temp_name=" ".join([people.firstname,people.secondname])
			names_people_in_system.append(temp_name)
		new_person_name=" ".join(['jacob','mutua'])
		self.assertTrue([new_person_name in names_people_in_system],msg="should add person to system")

	def test_add_person_not_fellow_or_staff_fails(self):
		invalid_person=self.implementation.add_person("james","mutua","watchman")
		self.assertEqual(invalid_person,"Not a valid person in our context")

	def test_add_person_with_name_having_numbers_fails(self):
		person_name_with_digits=self.implementation.add_person("mbuvi123242","meshack","fellow")
		self.assertEqual(person_name_with_digits,"Not a valid person in our context")

	def test_print_allocations(self):
		pass

	def test_add_existing_person_fails(self):
		person=self.implementation.add_person("meshack","Mbuvi","Fellow")
		self.assertEqual(person,"person already in the system")

	


		

		
unittest.main()