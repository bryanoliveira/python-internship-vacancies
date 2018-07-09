import model
from view import View

class Controller(object):
    def __init__(self, _option = 0):
        self._option = _option

    def factory(type, *args):

        if type == View._main:
            return MainMenu()

        elif type == View._area:
            return AreaSelect()

        elif type == View._course:
            return CourseSelect(args[0])

        elif type == View._mural:
            print(args[0])
            return CourseMural(args[0])

        elif type == View._registration:
            return RegistrationMenu()

    factory = staticmethod(factory)

class MainMenu(Controller):
    def act(self):
        menu = model.get_main_menu()
        view = View.factory(View._main)
        option = view.show_list(menu)

        if option == 1:
            return View._registration

        elif option == 2:
            return View._area

        elif option == 3:
            return None


class AreaSelect(Controller):
    def act(self):
        areas = model.get_areas()
        view = View.factory(View._area)
        option = view.show_list(areas)

        if option == None:
            return None
        elif option == View._back:
            return View._back
        else:
            return View._course, option


class CourseSelect(Controller):
    def act(self):
        courses = model.get_courses(self._option)
        view = View.factory(View._course)
        option = view.show_list(courses)

        if option == None:
            return None
        elif option == View._back:
            return View._back
        else:
            return View._mural, option


class CourseMural(Controller):
    def act(self):
        mural = model.get_internships(self._option)
        view = View.factory(View._mural)
        option = view.show_list(mural)

        if option == None:
            return None
        elif option == View._back:
            return View._back
        else:
            return None

class RegistrationMenu(Controller):
    def act(self):
        view = View.factory(View._registration)
        internship = view.get_informations()

        if internship == None:
            return None
        elif internship == View._back:
            return View._back
        else:
            save = model.Internship(internship[0], internship[1], internship[2])
            model.save_internship(save)

            option = view.show_success()

            if option == None:
                return None
            elif option == View._back:
                return View._back
            else:
                return None