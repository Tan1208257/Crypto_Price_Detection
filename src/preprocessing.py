def clean_data(df):
    return df.drop_duplicates().dropna()
