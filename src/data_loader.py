import pandas as pd
from pathlib import Path

def load_and_merge_data(data_dir):
    dfs = []
    for file in Path(data_dir).glob("*.csv"):
        df = pd.read_csv(file)
        symbol = file.stem.split("_")[1]
        df["symbol"] = symbol
        dfs.append(df)

    df = pd.concat(dfs, ignore_index=True)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")
    return df
