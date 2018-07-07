from controller import Controller

def route(new_route):

    if new_route[0] == "course menu":
        return Controller.factory(new_route[0], new_route[1])
    elif new_route[0] == "mural":
        return Controller.factory(new_route[0], new_route[1])
    else:
        return Controller.factory(new_route)
