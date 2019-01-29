# U06_Ex01_OldMacDonald.py
#
# Author: Donovan Ray
# Course: Coding for OOP
# Section: A2
#     Date: 12 Jan 2019
#      IDE: PyCharm
#
# Assignment Info
#   Exercise: OldMacDonald 01
#     Source: Python Programming
#    Chapter: #06
#
# Program Description
#   This program will print out the lyrics to Old MacDonald
#
#
#
# Algorithm (pseudocode)
#   Func1: OldMacDonald
#       return old mac donald had a farm
#   Func2: Eieio
#       return Ee-igh Ee-igh Oh!
#   Func3: Animal
#       make list and selector for list
#       for i in range 5
#           select animal from list
#           plait by space
#           print lyrics, with animal selected from list


def OldMacDonald():
    return 'Old MacDonald had a farm'

def Eieio():
    return 'Ee-igh Ee-igh Oh!'

def Animal():
    AnimalList = ['Cow moo', 'Pig oink', 'Duck quack', 'Chicken cluck', 'Lamb baa']
    return AnimalList

def Sing():
    sel = 0
    for i in range(5):
        animal = Animal()
        MacDon = OldMacDonald()
        Ei = Eieio()
        animalselect = animal[sel]
        animal = animalselect.split(' ')
        print('\n{2}\n{3}\nAnd on that farm he had a {0}, Ee-Igh Ee-Igh Oh! \nWith a {1} {1} '
              'here and a {1} {1} There. Here a {1} there a {1} everywhere a {1}, {1}.\n'
              '{2} {3}\n'.format(animal[0], animal[1], MacDon, Ei))
        sel = sel + 1


Sing()
