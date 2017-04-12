class Person():
	def __init__(self,firstname,secondname,person_type):
		self.firstname=firstname
		self.secondname=secondname
		self.persons=person_type
		self.office_name=""

	
class Fellow(Person):
	def __init__(self,firstname,secondname,person_type):
		self.person_type="Fellow"
		Person.__init__(self,firstname,secondname,self.person_type)
		self.livingspaceNumber=""
		
	
class Staff(Person):
	def __init__(self,firstname,secondname,person_type):
		self.person_type="staff"
		Person.__init__(self,firstname,secondname,self.person_type)

	

