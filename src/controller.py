import model
from view import View

class Controller(object):
    option = 0

    def factory(type, *args):

        if type == "main menu":
            return MainMenu()
        elif type == "area menu":
            return AreaSelect()
        elif type == "course menu":
            __class__.option = args[0]
            print(__class__.option)
            return CourseSelect()
        elif type == "course mural":
            __class__.option = ""
            __class__.option = args[0]
            print(__class__.option)
            return CourseMural()

    factory = staticmethod(factory)

    def options():
        return __class__.option

class MainMenu(Controller):
    def act(self):
        menu = model.get_main_menu()
        view = View.factory("main menu")
        option = view.show_list(menu)

        if option == 1:
            return ""
        elif option == 2:
            return "area menu"
        elif option == 3:
            print("Até Mais!\n")
            return None


class AreaSelect(Controller):
    def act(self):
        areas = model.get_areas()
        view = View.factory("area menu")
        option = view.show_list(areas)

        return "course menu", option



class CourseSelect(Controller):
    def act(self):
        courses = model.get_courses(Controller.options())
        view = View.factory("course menu")
        option = view.show_list(courses)

        return "course mural", option


class CourseMural(Controller):
    def act(self):
        mural = model.get_internships(Controller.options())
        view = View.factory("course mural")
        option = view.show_list(mural)

        return
