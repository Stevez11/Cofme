import request, exel_filler


def start():
    data = request.get_data()
    exel_filler.update_data(data)


if __name__ == "__main__":
    start()
