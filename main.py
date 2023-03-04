from cofme.project.mining_income_statistics import exel_filler, req
import json


def start():
    with open('../../private/hashrate_on_triple_minning.json') as f:
        json_obj = json.load(f)

    data = req.get_data(ethash_hash_rate=json_obj["ethash"],
                        kas_hash_rate=json_obj["kas"],
                        consumption=json_obj["consumption"])
    exel_filler.update_data(data)
