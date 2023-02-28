import json
import os
import shutil
import glob


def screen() -> None:
    with open("../../private/last_update.json") as f:
        json_obj = json.load(f)
    date = '-'.join(map(str, [json_obj['day'], json_obj['month'], json_obj['year']]))

    if os.path.exists(f"../../private/exel_archive/{date}.xlsx"):
        os.remove(f"../../private/exel_archive/{date}.xlsx")

    shutil.copy2("../../private/m2023.xlsx", "../../private/exel_archive")
    os.rename("../../private/exel_archive/m2023.xlsx",
              f"../../private/exel_archive/{date}.xlsx")
