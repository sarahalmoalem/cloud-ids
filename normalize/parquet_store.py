import pandas as pd
import duckdb


def save_parquet(rows):
    """
    Save normalized events to Parquet.
    Removes duplicate events using event_id.
    """

    if not rows:
        return

    df = pd.DataFrame(rows)

    if "event_id" in df.columns:
        df = df.drop_duplicates(subset=["event_id"])

    df["date"] = df["time"].str[:10]

    df.to_parquet(
        "data/parquet",
        partition_cols=["date"],
        index=False
    )


def query_events():
    """
    Query Parquet files using DuckDB.
    """

    return duckdb.sql("""
        SELECT
            event_name,
            COUNT(*) AS n
        FROM read_parquet(
            'data/parquet/**/*.parquet',
            hive_partitioning = true
        )
        GROUP BY 1
        ORDER BY n DESC
    """).df()


if __name__ == "__main__":
    sample_rows = [
        {
            "event_id": "1",
            "time": "2026-11-03T10:00:00Z",
            "event_name": "CreateBucket"
        },
        {
            "event_id": "2",
            "time": "2026-11-03T10:01:00Z",
            "event_name": "CreateBucket"
        },
        {
            "event_id": "3",
            "time": "2026-11-03T10:02:00Z",
            "event_name": "DeleteBucket"
        }
    ]

    save_parquet(sample_rows)

    print(query_events())