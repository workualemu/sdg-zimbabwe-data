import pandas as pd

def alter_data(df):
    # Drop the non-numeric rows.
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
    df.dropna(subset=['Value'], inplace=True)
    # Trim all whitespace.
    for col in df.select_dtypes(include=['object', 'string']).columns:
        df[col] = df[col].str.strip()
    return df
