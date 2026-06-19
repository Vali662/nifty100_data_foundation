import pandas as pd

def load_excel(file_path, sheet_name=0):
    df = pd.read_excel(
        file_path,
        sheet_name=sheet_name,
        skiprows=1
    )
    return df