from class_implementation import Implementation

def run():
	ob=Implementation()
	#create several offices and living spaces
	#ob.create_room('Blue','Office')
	ob.create_room('Black','Office')
	ob.create_room('Black','livingspace')
	#add several people
	ob.add_person("Meshack","mbuvi","Fellow")
	ob.add_person("Josephat","Musyoka","Fellow")

	ob.print_room("Black")

run()