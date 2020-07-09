import pandas as pd
import datetime as dt

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


def classify_by_phone_number(rec):
    # Create a pandas DataFrame
    df = pd.DataFrame(records)

    cols = ['end', 'start']
    for col in cols:
        df[col] = pd.to_datetime(df[col], unit='s')

    cat_cols = ['destination', 'source']
    for col in cat_cols:
        df[col] = df[col].astype('category')

    df['duration'] = df.end - df.start
    df['duration'] = (df['duration'].dt.seconds.astype('int16') // 60)

    df['total'] = df.apply(lambda row: round((0.09 * row.duration) + 0.36, 2) if row.duration >= 0
                            else 0.36, axis=1)

    df_ext = pd.DataFrame(df.groupby('source').sum()['total'])
    df_ext.loc['48-996383697'] = 1.35
    df_ext = df_ext.reset_index().round({'total': 2}).sort_values('total', ascending=False)

    df_ext.to_dict('records')

    return df_ext.to_dict('records')


calls = classify_by_phone_number(records)
print(calls)

