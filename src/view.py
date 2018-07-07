import os


class View(object):
    def factory(type):
        os.system('cls' if os.name == 'nt' else 'clear')

        if type == "main menu":
            return MainMenu()
        elif type == "area menu":
            return AreaSelect()
        #elif type == "course menu":
            #return CourseSelect()

    factory = staticmethod(factory)


class MainMenu(View):
    def show_list(options):
        #os.system('cls' if os.name == 'nt' else 'clear')
        print (options[0]+'\n')
        for options_number in range(1, len(options)):
            print(str(options_number) + ". " + options[options_number])

        option = int(input('\n: '))
        return option

    show_list = staticmethod(show_list)


class AreaSelect(View):
    def show_list(areas):
        #os.system('cls' if os.name == 'nt' else 'clear')
        print (areas[0] + '\n\n' + areas[1])
        for area_number in range(2, len(areas)):
            print(str(area_number-1) + ". " + areas[area_number])

        option = int(input("\n: "))
        return option

    show_list = staticmethod(show_list)

'''
class CourseSelect(View):
    def show_list(courses):
        #os.system('cls' if os.name == 'nt' else 'clear')
        print (courses[0] + '\n\n' + courses[1])

        for courses_number in range(0, len(courses[])):
            print(str(area_number-1) + ". " + areas[area_number])

        option = int(input("\n: "))
        return option

    show_list = staticmethod(show_list)
'''
