def create_features(df):
    df = df.copy()

    df["return"] = df["close"].pct_change()
    df["volume_change"] = df["volume"].pct_change()

    for w in [5, 10, 20]:
        df[f"return_mean_{w}"] = df["return"].rolling(w).mean()
        df[f"return_std_{w}"] = df["return"].rolling(w).std()

    df["target"] = (df["close"].shift(-1) > df["close"]).astype(int)
    return df.dropna()
