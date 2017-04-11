import unittest
from allocation import Room, Office,Person


class TestCreateRoom(unittest.TestCase):
	"""docstring for inheritanceTests"""
	
	def test_create_room_successfully(self):
		room=Room()
		initial_room_count=len(room.all_rooms)
		blue_office=room.create_room("Office","Blue")
		self.assertTrue(blue_office)
		new_room_count=len(room.all_rooms)
		self.assertEqual(new_room_count-initial_room_count,1)
	def test_add_person_successfully(self):
		self.person=Person()
		initial_person_count=len(self.person.persons)
		person=self.person.add_person("name","Fellow")
		self.assertTrue(person)
		new_person_count=len(person.persons)
		self.assertEqual(new_person_count-initial_person_count,1)
class TesstCreateOffice(unittest.TestCase):
	def test_office_ia_a_room(self):
		self.office=Office()
		self.room=Room()
		self.assertTrue(isinstance(self.office,Room),msg="Office should be a object of room")

	def test_office_allocation(self):
		self.office=Office()
		self.assertEqual(self.office.allocate_room("blue"),"Office allocated successfully")


		
unittest.main()