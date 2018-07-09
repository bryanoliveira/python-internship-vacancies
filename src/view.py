import os

_system_name = "\033[1;37mCENTRAL DE ESTÁGIOS\033[0m"

class View(object):

    _main = "main menu"
    _area = "area menu"
    _course = "course menu"
    _mural = "course mural"
    _registration = "registration menu"
    _back = "go back"

    def factory(type):
        os.system('cls' if os.name == 'nt' else 'clear')

        if type == __class__._main:
            return MainMenu()

        elif type == __class__._area:
            return AreaSelect()

        elif type == __class__._course:
            return CourseSelect()

        elif type == __class__._mural:
            return CourseMural()

        elif type == __class__._registration:
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

            option = str(input("\n[Para sair do programa: 'sair']\n: "))

            if option == "sair":
                return None

            try:
                option = int(option)
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("**Entrada inválida!**")
                continue

            if 0 < option < len(options):
                return option
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("**Entrada inválida!**")
                continue


class AreaSelect(View):
    def show_list(self, options):

        while True:
            print (_system_name + " - " + options[0] + '\n\n' + options[1])
            for area_number in range(2, len(options)):
                print(str(area_number - 1) + ". " + options[area_number])

            option = str(input("\n[Para sair do programa: 'sair' | Para voltar: 'voltar' ]\n: "))
            
            if option == "sair":
                return None
            elif option == "voltar":
                return self._back

            try:
                option = int(option)
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("**Entrada inválida!**")
                continue

            if 0 < option < len(options) - 1:
                return option
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("**Entrada inválida!**")
                continue


class CourseSelect(View):
    def show_list(self, options):

        while True:
            print (_system_name + " - " + options[0] + '\n\n' + options[1])

            for course_number in range(2, len(options)):
                print(str(course_number-1) + ". " + options[course_number])

            option = str(input("\n[Para sair do programa: 'sair' | Para voltar: 'voltar' ]\n: "))

            if option == "sair":
                return None
            elif option == "voltar":
                return self._back
            
            try:
                option = int(option)
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("**Entrada inválida!**")
                continue

            if 0 < option < len(options) - 1:
                return options[option + 1]
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("**Entrada inválida!**")
                continue


class CourseMural(View):
    def show_list(self, options):

        while True:
            print (_system_name + " - MURAL\n\n")

            for internship in options:
                internship.show()

            if len(options) == 0:
                print("Nenhuma vaga para este curso.")

            option = str(input("\n[Para sair do programa: 'sair' | Para voltar: 'voltar' ]\n: "))

            if option == "sair":
                return None
            elif option == "voltar":
                return self._back
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("**Entrada inválida!**")
                continue

class RegistrationMenu(View):
    def get_informations(self):

        while True:
            print(_system_name + " - CADASTRO DE VAGAS\n")
            name = str(input("Título da vaga: "))
            description = str(input("Descrição detalhada: "))
            courses = str(input("Cursos aceitos (separados por vírgula e um espaço): "))

            os.system('cls' if os.name == 'nt' else 'clear')

            print(_system_name + " - CADASTRO DE VAGAS\n")
            print("NOVA VAGA:\nNome: " + name + "\nDescrição: " + description + "\nCursos: " + courses)

            print("\n\nVocê gostaria de:")
            print("1. Salvar as informações")
            print("2. Editar as informações")
            
            option = str(input("\n[Para sair do programa: 'sair' | Para voltar: 'voltar' ]\n: "))

            if option == "sair":
                return None
            elif option == "voltar":
                return self._back

            try:
                option = int(option)
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("**Entrada inválida!**")
                continue

            if option == 1:
                break
            elif option == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("**Editando informações!**")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("**Entrada inválida!**")


        os.system('cls' if os.name == 'nt' else 'clear')

        internship = [name, description, courses]
        return internship

    def show_success(self):
        while True:
            print(_system_name + " - CADASTRO DE VAGAS\n")
            print("Vaga cadastrada com sucesso!\n")
            option = str(input("\n[Para sair do programa: 'sair' | Para voltar: 'voltar' ]\n: "))

            if option == "sair":
                return None
            elif option == "voltar":
                return self._back
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("**Entrada inválida!**")
                continue
