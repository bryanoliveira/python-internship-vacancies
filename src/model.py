import json

## MODELOS

class Internship(object):
    def __init__(self, name, description, courses): # string, string, string list
        self.name = name
        self.description = description
        self.courses = courses

class MementoCaretaker(object):
    def __init__(self):
        self.history = []

    # o controller não possui um estado específico, só é necessário salvar sua instância
    def save(self, controller):
        self.history.append(controller)

    def undo(self):
        controller = self.history[-1]
        self.history.pop()
        return controller

## CONSTANTES

_menu_main_location = "databases/main.json"
_menu_areas_location = "databases/areas.json"
_menu_courses_location = "databases/courses.json"
_menu_internships_location = "databases/internships.json"
_memento = MementoCaretaker()

## AUXILIARES

def readlines(file_name): # string
    file = open(file_name, 'r')
    lines = json.load(file)
    return lines

## INTERFACES

def go_back():
    return _memento.undo()

def save_state(controller):
    _memento.save(controller)

def get_main_menu():
    menu = readlines(_menu_main_location)
    return menu

def get_areas():
    areas = readlines(_menu_areas_location)
    return areas

def get_courses(area_id): # int
    all_courses = readlines(_menu_courses_location)

    courses = []
    courses.append(all_courses[0])
    courses.append(all_courses[1])
    for course in all_courses[1+area_id]:
        courses.append(course)

    return courses

def save_internship(internship): # Internship object
    file = open(_menu_internships_location, 'r+')
    internships = json.load(file)
    internships += internship
    json.dump(file, internships)

def get_internships(course): # course string
    file = open(_menu_internships_location, 'r')
    all_internships = json.load(file)
    internships = []
    internships.append(all_internships[0])
    internships.append(all_internships[1])
    del all_internships[0:2]
    for internship in all_internships:
        if course in internship.courses:
            internships += internship

    return internships
