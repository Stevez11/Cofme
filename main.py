import request, exel_filler


def start_program():
    data = request.get_data()
    exel_filler.update_data(data)


if __name__ == "__main__":
    start_program()
