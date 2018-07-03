import model

class AreaMenu:

    def act(self):
        areas = model.get_areas()
        view.show_list(areas)
        new_area = int(input("Qual área [1 .. " + str(len(areas)) + "]? "))