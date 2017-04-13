class Person():
	def __init__(self,firstname,secondname,person_type):
		self.firstname=firstname
		self.secondname=secondname
		self.persons=person_type
		self.office_name=""
		self.wants_accommodation=""


	
class Fellow(Person):
	def __init__(self,firstname,secondname,person_type):
		self.person_type="FELLOW"
		Person.__init__(self,firstname,secondname,self.person_type)
		self.livingspaceName=""

		
	
class Staff(Person):
	def __init__(self,firstname,secondname,person_type):
		self.person_type="STAFF"
		Person.__init__(self,firstname,secondname,self.person_type)

	

