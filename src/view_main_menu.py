def show_greetings():
    print("CENTRAL DE ESTÁGIOS - PROGRAD - MURAL DE OPORTUNIDADES")

def show_list(areas):
    for area_number in range(0, len(areas)):
        print(str(area_number + 1) + ". " + areas[area_number])