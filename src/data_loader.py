import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def load_names():
    df = pd.read_csv(DATA_DIR / "names_extended.csv")
    df.columns = df.columns.str.strip()
    return df

def load_cities():
    df = pd.read_csv(DATA_DIR / "cities_extended.csv")
    df.columns = df.columns.str.strip()
    return df

def load_merchants():
    df = pd.read_csv(DATA_DIR / "merchants_extended.csv")
    df.columns = df.columns.str.strip()
    return df

def load_addresses():
    df = pd.read_csv(DATA_DIR / "addresses_extended.csv")
    df.columns = df.columns.str.strip()
    return df