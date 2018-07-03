from controller_main_menu import MainMenu
from controller_area_select import AreaMenu

def route(new_route):
    if new_route == "main menu":
        return MainMenu()
    elif new_route == "area menu":
        return AreaMenu()
    else:
        return None