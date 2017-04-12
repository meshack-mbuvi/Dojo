import unittest
from class_implementation import Implementation


class TestCreateRoom(unittest.TestCase):
	"""docstring for inheritanceTests"""
	def test_create_room_successfully(self):
		self.imple=Implementation()
		self.imple.create_room("White","Office")
		initial_room_count=len(self.imple.all_rooms)
		office=self.imple.create_room("Red","Livingspace")
		self.assertTrue(office)
		new_room_count=len(self.imple.all_rooms)
		self.assertEqual(new_room_count-initial_room_count,1)

	def test_add_person_successfully(self):
		self.imple=Implementation()
		initial_person_count=len(self.imple.all_people)
		self.person=self.imple.add_person("meshack","mbuvi","Fellow")
		self.assertTrue(self.person)
		new_person_count=len(self.imple.all_people)
		self.assertEqual(new_person_count-initial_person_count,1)

	def test_allocate_office_successfuly(self):
		obj=Implementation()
		mbuvi=obj.add_person("meshack","Mbuvi","Fellow")
		obj.create_room("Blue","Office")
		allocations=obj.allocate_office(mbuvi)
		#No office exist so allocation cannot be done
		self.assertNotEqual(allocations['office'],None,msg="Mbuvi has to be allocated office")

	def test_allocate_livingspace_fails(self):
		obj=Implementation()
		josep=obj.add_person("Joseph","mbenge","staff")
		room=obj.create_room("White","Livingspace")
		space=obj.allocate_livingspace(josep)
		self.assertEqual(space,None,josep.livingspacename)

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
		
		# print(self.obj.all_rooms[0].list_of_occupants)
		# print("Done")
		

		
unittest.main()