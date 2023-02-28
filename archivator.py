import json
import os
import shutil
import glob


def screen() -> None:
    with open("last_update.json") as f:
        json_obj = json.load(f)
    date = '-'.join(map(str, [json_obj['day'], json_obj['month'], json_obj['year']]))

    if os.path.exists(f"exel_archive/{date}.xlsx"):
        os.mkdir(f"{date}")
        shutil.move(f"exel_archive/{date}.xlsx", f"exel_archive/{date}/{date}.xlsx")
        os.rename(f"exel_archive/{date}/{date}.xlsx",
                  f"exel_archive/{date}/1.xlsx")

    elif os.path.exists(f"exel_archive/{date}"):
        shutil.copy2("m2023.xlsx", f"exel_archive/{date}")
        os.rename("exel_archive/m2023.xlsx", f"exel_archive/{len(glob.glob('/exel_archive/*')) + 1}.xlsx")

    else:
        shutil.copy2("m2023.xlsx", "exel_archive")
        os.rename("exel_archive/m2023.xlsx",
                  f"exel_archive/{date}.xlsx")
