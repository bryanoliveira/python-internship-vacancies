from controller import Controller
from controller import View
import model

def route(actual_route, new_route):

    if new_route == View._back:
        return model.go_back()
    elif type(new_route) is tuple and (new_route[0] == View._course or new_route[0] == View._mural):
        new_controller = Controller.factory(new_route[0], new_route[1])
    else:
        new_controller = Controller.factory(new_route)

    model.save_state(actual_route)
    
    return new_controller