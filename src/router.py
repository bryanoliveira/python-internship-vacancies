from controller import Controller

def route(new_route):

    if type(new_route) is tuple:
        if new_route[0] == "course menu" or new_route[0] == "course mural":
            return Controller.factory(new_route[0], new_route[1])
    else:
        return Controller.factory(new_route)
