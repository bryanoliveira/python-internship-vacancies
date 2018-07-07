import router
from controller import Controller


# rota principal
def main():
    
    controller = router.route("main menu")

    while True:
        controller = router.route(controller.act())
        if controller == None:
            break


if __name__ == "__main__":
    main()
