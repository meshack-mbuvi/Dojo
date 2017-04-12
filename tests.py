import unittest
from class_implementation import Implementation


class TestCreateRoom(unittest.TestCase):
	"""docstring for inheritanceTests"""
	def test_create_room_successfully(self):
		self.class_object=Implementation()
		self.class_object.create_room("White","Office")
		initial_room_count=len(self.class_object.all_rooms)
		office=self.class_object.create_room("Red","Livingspace")
		self.assertTrue(office)
		new_room_count=len(self.class_object.all_rooms)
		self.assertEqual(new_room_count-initial_room_count,1)

	def test_add_person_successfully(self):
		self.class_object=Implementation()
		initial_person_count=len(self.class_object.all_people)
		self.person=self.class_object.add_person("meshack","mbuvi","Fellow")
		self.assertTrue(self.person)
		new_person_count=len(self.class_object.all_people)
		self.assertEqual(new_person_count-initial_person_count,1)

	def test_allocate_office_successfuly(self):
		obj=Implementation()
		mbuvi=obj.add_person("meshack","Mbuvi","Fellow")
		obj.create_room("Blue","Office")
		allocations=obj.allocate_office(mbuvi)
		#No office exist so allocation cannot be done
		self.assertNotEqual(allocations['office'],None,msg="Mbuvi has to be allocated office")


class TestCheckRooms(unittest.TestCase):
	"""docstring for TestCheckRooms"""
	
	def test_prints_room_name(self):
		self.obj=Implementation()
		#create room first
		self.room=self.obj.create_room("White","office")
		#add several people
		self.obj.add_person("Meshack","mbuvi","Fellow")
		self.obj.add_person("Josephat","Musyoka","Fellow")
		
		self.josep=self.obj.add_person("Joseph","mbenge","staff")
		
		occupants=self.obj.print_room("White")
		self.assertEqual(occupants,['Meshack mbuvi', 'Josephat Musyoka', 'Joseph mbenge'],msg='Should print the names of people allocated to white office')
		print occupants
		
	def test_prints_allocations(self):
		pass
		

		
unittest.main()