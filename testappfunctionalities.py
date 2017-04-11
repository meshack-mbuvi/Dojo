#!/usr/bin/env python
"""
Commandline application using docopt
usage:

"""
from docopt import docopt
from dojo import Dojo
from allocation import Dojo,Room,Office,LivingSpace,Person
"""Instantiate the classes
"""
dojo=Dojo()

office=Office()
livingspace=LivingSpace()
"""A list with objects of type room
One can loop over this list retrieving each object 
"""
rooms=[]
people=[]

def main():
        names=["Blue","Black"]
        create_room("Office",names)
        names=["Meshack"]
        add_person(names,"Staff")
        print(len(rooms))
        for room_index in range(0,len(rooms)):
                print(rooms[room_index].room_name)

        for people_index in range(0,len(people)):
                print(people)

        
def create_room(room_type,room_name):
        """This function calls the functonalities on room object, looping through a list of names"""
        for index in range(0,len(room_name)):
                '''loop through the room_name list while creating the room objects'''
                room=Room()#This object should be created each time we want to work on it
                if room_type.lower()=="office":
                        '''Create room object and append it to a list rooms'''
                        rooms.append(room.create_room(room_type,room_name[index]))
                        print(room_name[index])
                        print("An office called %s has been successfully created" % room_name[index])
                elif room_type.lower()=="livingspace":
                        rooms.append(room.create_room(room_type,room_name[index]))
                        print("A livingspace called %s has been successfully created" % room_name[index])
                else:
                        print("Not a valid room")

def add_person(name,person_type,accom='N'):
        """if person is Fellow s/he can allocated both an office and livingspace"""
        if person_type.lower()=='staff':
                pass
        person=Person()
        people.append(person.add_person(name,person_type))
                        
main()
