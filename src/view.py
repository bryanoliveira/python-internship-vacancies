import os

_system_name = "CENTRAL DE ESTÁGIOS"

class View(object):

    main = "main menu"
    area = "area menu"
    course = "course menu"
    mural = "course mural"
    registration = "registration menu"

    def factory(type):
        os.system('cls' if os.name == 'nt' else 'clear')

        if type == __class__.main:
            return MainMenu()

        elif type == __class__.area:
            return AreaSelect()

        elif type == __class__.course:
            return CourseSelect()

        elif type == __class__.mural:
            return CourseMural()

        elif type == __class__.registration:
            return RegistrationMenu()

        else:
            return

    factory = staticmethod(factory)


class MainMenu(View):
    def show_list(self, options):

        while True:
            print (_system_name + " - " + options[0] + '\n')
            for options_number in range(1, len(options)):
                print(str(options_number) + ". " + options[options_number])

            option = int(input('\n: '))
            if option > 0 and option < 4:
                return option
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("**Entrada inválida!**")
                continue


class AreaSelect(View):
    def show_list(self, areas):

        while True:
            print (_system_name + " - " + areas[0] + '\n\n' + areas[1])
            for area_number in range(2, len(areas)):
                print(str(area_number-1) + ". " + areas[area_number])

            option = str(input("\n[Para sair do programa: 'sair' | Para voltar: 'voltar' ]\n: "))
            if option == "sair":
                return None
            elif option == "voltar":
                return None
            else:
                option = int(option)
                if option > 0 and option < len(areas)-2:
                    return option
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("**Entrada inválida!**")
                    continue


class CourseSelect(View):
    def show_list(self, courses):

        while True:
            print (_system_name + " - " + courses[0] + '\n\n' + courses[1])

            for course_number in range(2, len(courses)):
                print(str(course_number-1) + ". " + courses[course_number])

            option = str(input("\n[Para sair do programa: 'sair' | Para voltar: 'voltar' ]\n: "))
            if option == "sair":
                return None
            elif option == "voltar":
                return None
            else:
                option = int(option)
                if option > 0 and option < len(courses)-2:
                    return courses[option+1]
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("**Entrada inválida!**")
                    continue


class CourseMural(View):
    #!TODO arrumar estrutura de visualização das vagas
    def show_list(self, mural):

        while True:
            print (_system_name + " - AREAS\n\n")

            option = str(input("\n[Para sair do programa: 'sair' | Para voltar: 'voltar' ]\n: "))
            if option == "sair":
                return None
            elif option == "voltar":
                return None
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("**Entrada inválida!**")
                continue

class RegistrationMenu(View):
    def get_informations(self):

        while True:
            print(_system_name + " - CADASTRO DE VAGAS\n")
            name = str(input("Nome: "))
            description = str(input("Descrição: "))
            courses = str(input("Cursos: "))

            os.system('cls' if os.name == 'nt' else 'clear')

            print(_system_name + " - CADASTRO DE VAGAS\n")
            print("VAGA\nNome: " + name + "\nDescrição: " + description + "\nCursos: " + courses)

            print("\n\nVocê gostaria de:")
            print("1. Salvar informações")
            print("2. Editar informações")
            print("3. Voltar ao menu anterior")
            print("4. Sair do programa")
            option = int(input("\n: "))

            if option == 1:
                break
            elif option == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("**Editando informações!**")
            elif option == 3:
                return None
            elif option == 4:
                return None
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("**Entrada innválida!**")


        os.system('cls' if os.name == 'nt' else 'clear')

        while True:
            print(_system_name + " - CADASTRO DE VAGAS\n")
            print("Vaga cadastrada com sucesso!\n")
            option = str(input("\n[Para sair do programa: 'sair' | Para voltar: 'voltar' ]\n: "))
            if option == "sair" or option == "voltar":
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("**Entrada inválida!**")
                continue

        internship = [option, name, description, courses]
        return internship
