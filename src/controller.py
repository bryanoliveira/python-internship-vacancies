import model
from view import View

class Controller(object):

    def factory(type, *args):
        if type == "main menu":
            return MainMenu()
        elif type == "area menu":
            return AreaSelect()
        elif type == "course menu":
            return CourseSelect(args)

    factory = staticmethod(factory)


class MainMenu(Controller):

    def act(self):
        menu = model.get_main_menu()

        view = View.factory("main menu")
        option = view.show_list(menu)

        if option == 1:
            return ""
        elif option == 2:
            return ""
        elif option == 3:
            return "area menu"


class AreaSelect(Controller):

    def act(self):
        areas = model.get_areas()

        view = View.factory("area menu")
        option = view.show_list(areas)

        return "course menu"


'''
class CourseSelect(Controller):

    def act(self):
        courses = model.get_courses()

        view = View.factory("course menu")
        option = view.show_list(courses)

        return "mural"
'''
