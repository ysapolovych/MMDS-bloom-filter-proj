import pandas as pd

def to_pandas(json_obj):
    return pd.json_normalize(json_obj)