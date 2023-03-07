import json
import os
import shutil


def screen() -> None:
    with open("../../private/last_update.json") as f:
        json_obj = json.load(f)

    date = '-'.join(map(str, [json_obj['day'], json_obj['month'], json_obj['year']]))

    os.rename("../../private/m2023.xlsx", f"../../private/{date}.xlsx")
    shutil.copy2(f"../../private/{date}.xlsx", f"../../private/exel_archive/")
    os.rename(f"../../private/{date}.xlsx", f"../../private/m2023.xlsx")
