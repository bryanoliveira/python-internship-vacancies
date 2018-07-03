import model
import view_main_menu as view

class MainMenu:
    
    def act(self):
        menu = model.get_main_menu()
        view.show_list(menu)
        option = view.get_option()
        if menu[int(option)] == ""