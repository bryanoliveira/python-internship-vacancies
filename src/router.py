from controller import Controller

def route(new_route):
    return Controller.factory(new_route)
