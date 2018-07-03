class View:
    def __init__(self):
        pass

    def show_list(self, data):
        for data_index in range(0, len(data)):
            print(str(data_index + 1) + ". " + data[data_index])