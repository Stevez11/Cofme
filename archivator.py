import json
import os
import shutil


def screen() -> None:
    with open("last_update.json") as f:
        json_obj = json.load(f)
    date = '-'.join(map(str, [json_obj['day'], json_obj['month'], json_obj['year']]))

    if os.path.exists(f"exel_archive/{date}.xlsx"):
        pass
    else:
        shutil.copy2("m2023.xlsx", "exel_archive")
        os.rename("exel_archive/m2023.xlsx",
                  f"exel_archive/{date}.xlsx")
