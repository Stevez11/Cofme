import json
import os
import shutil


def screen() -> None:
    shutil.copy2("m2023.xlsx", "exel_archive")
    with open("last_update.json") as f:
        json_obj = json.load(f)
    os.rename("exel_archive/m2023.xlsx",
              f"exel_archive/{'-'.join(map(str, [json_obj['day'], json_obj['month'], json_obj['year']]))}.xlsx")

