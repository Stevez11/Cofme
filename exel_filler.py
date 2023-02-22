import datetime
import openpyxl
import pandas as pd
import json
import archivator


def update_data(df: pd.DataFrame, month=-1):
    assert type(month) == int, "Incorrect data type transmitted in month"
    archivator.screen()
    book = openpyxl.load_workbook("m2023.xlsx")
    book.active = month
    sheet = book.active

    for date, day, ethw, zil, kas, cons in zip(df['Date'], df['day'], df['ETHW reward'], df['ZIL reward'],
                                               df['KAS reward'],
                                               df['consumption']):

        if sheet[f"A{day + 1}"].value == date:
            sheet[f"C{day + 1}"].value = ethw.replace('.', ',')
            sheet[f"D{day + 1}"].value = zil.replace('.', ',')
            sheet[f"E{day + 1}"].value = kas
            sheet[f"J{day + 1}"].value = cons * 1000

    book.save("m2023.xlsx")

    with open('last_update.json') as f:
        json_obj = json.load(f)
    json_obj['day'] = datetime.datetime.now().date().day - 1
    json_obj['month'] = datetime.datetime.now().date().month
    with open('last_update.json', 'w') as f:
        json.dump(json_obj, f)

    book.close()


