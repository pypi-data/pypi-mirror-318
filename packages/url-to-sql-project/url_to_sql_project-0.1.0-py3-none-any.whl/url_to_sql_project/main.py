import pandas as pd
import pyodbc
import requests
from io import StringIO

def download_data(url: str) -> pd.DataFrame:
    """
    Downloads CSV data from the provided URL and returns it as a pandas DataFrame.
    """
    response = requests.get(url)
    response.raise_for_status()
    return pd.read_csv(StringIO(response.text))

def insert_data_to_sql(df: pd.DataFrame, server: str, database: str, username: str, password: str, table: str):
    """
    Inserts the provided DataFrame into a SQL Server database.
    """
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    for _, row in df.iterrows():
        sql = f"INSERT INTO {table} ({', '.join(df.columns)}) VALUES ({', '.join(['?' for _ in row])})"
        cursor.execute(sql, tuple(row))

    conn.commit()
    conn.close()

def main(url: str, server: str, database: str, username: str, password: str, table: str):
    """
    Main function to download data from the URL and insert it into SQL Server.
    """
    df = download_data(url)
    insert_data_to_sql(df, server, database, username, password, table)
