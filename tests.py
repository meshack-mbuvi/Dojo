import unittest
from class_implementation import Implementation


class TestCreateRoom(unittest.TestCase):
	"""docstring for inheritanceTests"""
	def setup(self):
		self.obj=Implementation()
		
	def test_create_room_successfully(self):
		self.imple=Implementation()
		self.imple.create_room("Blue","Office")
		initial_room_count=len(self.imple.all_rooms)
		blue_office=self.imple.create_room("Blue","Livingspace")
		self.assertTrue(blue_office)
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
		
		allocations=obj.allocate_office("Mbuvi")
		#No office exist so allocation cannot be done
		self.assertEqual(allocations['office'],None,msg="Mbuvi has to be allocated office")

	def test_allocate_livingspace_fails(self):
		obj=Implementation()
		josep=obj.add_person("Joseph","mbenge","staff")
		room=obj.create_room("White","Livingspace")
		space=obj.allocate_livingspace(josep)
		self.assertEqual(space,None,josep.livingspacename)

class TestCheckRooms(unittest.TestCase):
	"""docstring for TestCheckRooms"""
	def __init__(self, arg):
		super(TestCheckRooms, self).__init__()
		self.arg = arg
		

		
unittest.main()