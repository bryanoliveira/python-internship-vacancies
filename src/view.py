import os


class View(object):
    def factory(type):
        os.system('cls' if os.name == 'nt' else 'clear')

        if type == "main menu":
            return MainMenu()
        elif type == "area menu":
            return AreaSelect()
        elif type == "course menu":
            return CourseSelect()
        elif type == "course mural":
            return CourseMural()
        else:
            return

    factory = staticmethod(factory)


class MainMenu(View):
    def show_list(options):
        print (options[0]+'\n')
        for options_number in range(1, len(options)):
            print(str(options_number) + ". " + options[options_number])

        option = int(input('\n: '))
        return option

    show_list = staticmethod(show_list)


class AreaSelect(View):
    def show_list(areas):
        print (areas[0] + '\n\n' + areas[1])
        for area_number in range(2, len(areas)):
            print(str(area_number-1) + ". " + areas[area_number])

        option = int(input("\n: "))
        return option

    show_list = staticmethod(show_list)


class CourseSelect(View):
    def show_list(courses):

        print (courses[0] + '\n\n' + courses[1])

        for course_number in range(2, len(courses)):
            print(str(course_number-1) + ". " + courses[course_number])

        option = int(input("\n: "))
        return courses[option+1]

    show_list = staticmethod(show_list)

class CourseMural(View):
    def show_list(mural):

        print (mural[0] + '\n\n' + mural[1])

        for mural_number in range(2, len(mural)):
            print(str(mural_number+1) + ". " + mural[mural_number])

        option = int(input("\n: "))
        return option

    show_list = staticmethod(show_list)
