import json

## MODELOS

class Internship(object):
    def __init__(self, name, description, courses): # string, string, string list
        self.name = name
        self.description = description
        if type(courses) is str:
            self.courses = [course.strip() for course in courses.split(',')]
        else:
            self.courses = courses

    def dump(self):
        me = []
        me.append(self.name)
        me.append(self.description)
        me.append(self.courses)

        return me

    
    def show(self):
        cslen = len("Cursos aceitos: ") + sum([len(course) for course in self.courses]) + 2 * len(self.courses) # tamanho da linha de cursos
        horiz = max([len(self.name), len(self.description), cslen]) + 1 # tamanho máximo de cada linha

        print("+" + "-" * horiz + "+")
        print("| \033[1;37m" + self.name + "\033[0m " * (horiz - len(self.name) - 1) + "|")
        print("+" + "-" * horiz + "+")
        print("| " + self.description + " " * (horiz - len(self.description) - 1) + "|")
        print("+" + "-" * horiz + "+")
        print("| " + "Cursos aceitos: ", end='')
        for course in self.courses[:-1]:
            print(course, end=', ')
        print(self.courses[-1] + " " * (horiz - cslen + 1) + "|")
        print("+" + "-" * horiz + "+\n")

class MementoCaretaker(object):
    def __init__(self):
        self.history = []

    # o controller não possui um estado específico, só é necessário salvar sua instância
    def save(self, controller):
        self.history.append(controller)

    def undo(self):
        if len(self.history) > 0:
            controller = self.history[-1]
            self.history.pop()
            return controller
        else:
            return None

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
    if controller != None:
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
    internships = []
    with open(_menu_internships_location, 'r') as file:
        internships = json.loads(file.read())
        file.close()

    internships.append(internship.dump())

    with open(_menu_internships_location, 'w') as file:
        file.write(json.dumps(internships))

def get_internships(course): # course string
    internships = []
    with open(_menu_internships_location, 'r') as file:
        all_internships = json.loads(file.read())

        print(all_internships)
        for t_internship in all_internships:
            internship = Internship(t_internship[0], t_internship[1], t_internship[2])
            if course in internship.courses:
                internships.append(internship)

        file.close()

    return internships