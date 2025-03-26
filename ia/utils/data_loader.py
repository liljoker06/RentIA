import pandas as pd

DATA_PATH = 'data/airbnb_filtered.parquet'

def load_data():
    try:
        df = pd.read_parquet(DATA_PATH)
        print (f"Donnée chargée depuis {DATA_PATH} ({len(df)} lignes)")
        return df
    except Exception as e:
        print(f"Erreur lors du chargement des données depuis {DATA_PATH}")
        print(e)
        return pd.DataFrame()

dataframe = load_data()


# Pour tester directement le chargement
# if __name__ == "__main__":
#     df = load_data()
#     print(df.head()) 
#     print(f"\nNombre total de lignes : {len(df)}")
#     print(f"Colonnes disponibles : {df.columns.tolist()}")
