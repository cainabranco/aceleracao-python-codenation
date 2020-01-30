import pandas as pd
import numpy as np

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564626000, 'start': 1564647600}
]


def classify_by_phone_number(records):
    # Create a pandas DataFrame
    df = pd.DataFrame(records)

    # Select columns to convert as Datetime
    datetime_columns = ['start', 'end']
    for i in datetime_columns:
        df[i] = pd.to_datetime(df[i], unit='s')

    # Change the tipe of duration
    df['duration'] = df['end'] - df['start']
    df['duration'] = df['duration'] / np.timedelta64(1, 'm')
    df['total'] = 0.36

    for i in df.index:
        if 6 <= (df['start'][i].hour) <= 22:
            df['total'][i] = df['total'][i] + (df['duration'][i] * 0.09)

    df.groupby(['source']).sum()

    return df[['source', 'total']].groupby('source').sum()


calls = classify_by_phone_number(records)
print(calls)
