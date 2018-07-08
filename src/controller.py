import model
from view import View

class Controller(object):
    option = 0

    def factory(type, *args):

        if type == View.main:
            return MainMenu()

        elif type == View.area:
            return AreaSelect()

        elif type == View.course:
            __class__.option = args[0]
            print(__class__.option)
            return CourseSelect()

        elif type == View.mural:
            __class__.option = ""
            __class__.option = args[0]
            print(__class__.option)
            return CourseMural()

        elif type == View.registration:
            return RegistrationMenu()

    factory = staticmethod(factory)

    def options():
        return __class__.option

class MainMenu(Controller):
    def act(self):
        menu = model.get_main_menu()
        view = View.factory(View.main)
        option = view.show_list(menu)

        if option == 1:
            return View.registration

        elif option == 2:
            return View.area

        elif option == 3:
            return None


class AreaSelect(Controller):
    def act(self):
        areas = model.get_areas()
        view = View.factory(View.area)
        option = view.show_list(areas)

        if option == None:
            return None
        else:
            return View.course, option


class CourseSelect(Controller):
    def act(self):
        courses = model.get_courses(Controller.options())
        view = View.factory(View.course)
        option = view.show_list(courses)

        if option == None:
            return None
        else:
            return View.mural, option


class CourseMural(Controller):
    def act(self):
        mural = model.get_internships(Controller.options())
        view = View.factory(View.mural)
        option = view.show_list(mural)

        if option == None:
            return None
        else:
            return None

class RegistrationMenu(Controller):
    def act(self):
        view = View.factory(View.registration)
        internship = view.get_informations()

        if internship == None:
            return None
        else:
            save = model.Internship(internship[1], internship[2], internship[3])
            #!TODO verficar erro ao salvar vaga
            #model.save_internship(save)


            if internship[0] == "sair":
                return None
            else:
                return None
