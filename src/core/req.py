import pandas as pd
import requests
import datetime
import json


def get_kas_data(kas_hash_rate):
    kas_req = requests.get(
        f'https://whattomine.com/coins/352.json?hr={kas_hash_rate}&p=0.0&fee=2.0&cost=0.0&cost_currency=USD&hcost=0.0&span_br=&span_d=3')
    data = kas_req.json()
    kas_rewards = float(data['estimated_rewards'])
    kas_rewards = round(kas_rewards, 2)
    return kas_rewards


def get_data(today=str(datetime.datetime.now().date()),
             ethash_hash_rate=None,
             kas_hash_rate=None,
             consumption=None) -> pd.DataFrame:
    assert type(consumption) in [int, float], "Incorrect data type transmitted in consumption"
    assert type(ethash_hash_rate) and type(
        kas_hash_rate) == int, "Incorrect data type transmitted in ethash_hash_rate or kas_hash_rate"

    with open('../../private/last_update.json') as f:
        json_obj = json.load(f)
    assert json_obj[
               'month'] <= datetime.datetime.now().date().month, "current_month cannot be less than last moth update"

    kas_rewards = get_kas_data(kas_hash_rate)

    req = requests.get(
        'https://billing.ezil.me/v2/accounts/0xab9a6d7f2340a6eb06cfa17bcc76d63a5b68e0e3.zil1sakzjjae30arff5aj5ekcpf793f622snjrayvv/revenue_report/mining_rewards/export?coin=ethw&sort_by=date&direction=desc&view_by=days')

    data = [i.lstrip() for i in req.text.split('\n')]

    while '' in data:
        data.remove('')

    df = pd.DataFrame([i.split(',') for i in data[1:]], columns=[i.lstrip() for i in data.pop(0).split(',')])

    df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d")
    df['month'] = pd.DatetimeIndex(df['Date']).month
    df['day'] = pd.DatetimeIndex(df['Date']).day
    df = df[
        (df.Date > '2022-12-31') & (df.Date > f"{json_obj['year']}-{json_obj['month']}-{json_obj['day']}") & (
                    df.Date != today)]
    df['KAS reward'] = round(df['Hashrate(MHs)'].astype(float) / ethash_hash_rate * kas_rewards, 2)
    df['consumption'] = round(df['Hashrate(MHs)'].astype(float) / ethash_hash_rate * consumption, 2)
    print(df)
    return df
