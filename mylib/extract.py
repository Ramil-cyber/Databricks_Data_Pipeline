import pandas as pd


def extract_csv(url):
    pd_df = pd.read_csv(url)

    print("Successfully extracted the CSV file")
    return pd_df


if __name__ == "__main__":
    extract_csv(
        "https://raw.githubusercontent.com/nogibjj/Ramil-Data-Pipeline-Databricks/refs/heads/main/data/Clubs.csv"
    )
