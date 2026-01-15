import pandas as pd

def load_csv(path):
    """
    This helps to load a CSV file from the given path and returns a pandas DataFrame.

    """
    try:
        df = pd.read_csv(path)
        print(f"[INFO] Loaded dataset successfully from {path}")
        return df
    except Exception as e:
        print("[ERROR] Could not load the dataset:", e)
        return None
